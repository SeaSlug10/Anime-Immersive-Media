from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from anime_database import AnimeData as db
import random as rand
import time

class Song:

    def __init__(self, path, name):
        self.db = db()
        self.path = path
        self.name = name[:name.index("-")]
        self.completed = False
        self.attempted = False

    def play(self, app, prev):
        self.attempted = True
        app.clear_frame()
        ttk.Button(app.mainframe, text="Back", command=lambda: self.back(app, prev)).grid(row=0, column=0)
        ttk.Label(app.mainframe, text="Guess: ").grid(row=1, column=0)
        self.entry = tk.Entry(app.mainframe, width=10, font=("Helvetica", 20))
        self.entry.grid(row=1, column=1)
        ttk.Button(app.mainframe, text="Enter", command = lambda:self.check_guess(app, prev)).grid(column=1, row=2)
        print(f"Now playing {str(self)}")

    def check_guess(self, app, prev):
        entered = self.db.get_anime_data(self.entry.get())["name_english"]
        actual = self.db.get_anime_data(self.name)["name_english"]
        if entered == actual:
            self.completed=True
            self.back(app, prev)
        else:
            self.entry.configure(bg="#ff9090")
            app.root.after(500, lambda: self.entry.configure(bg='white'))

    def back(self, app, prev):
        prev.display_difficulty(app)

    def __str__(self):
        return f"{self.name}, attempted: {self.attempted}, completed: {self.completed}"

class SongDifficulty:

    def __init__(self, songs, name):
        self.songs = songs
        self.name = name

    def display_difficulty(self, app):
        app.clear_frame()
        ttk.Button(app.mainframe, text="Back", command = app.main_menu).grid(column=0, row=0)
        ttk.Button(app.mainframe, text="Random", command = lambda : self.play_random(app)).grid(column=1, row=0)
        ttk.Label(app.mainframe, text="Select a song").grid(column=0, row=1)
        for i in range(len(self.songs)):
            buttonColor = lambda song: "light green" if song.completed else "#909090" if song.attempted else "white"
            buttonLabel = lambda i: f"Song {i+1} - {self.songs[i].name}" if self.songs[i].completed else f"Song {i+1}"
            tk.Button(app.mainframe, text=buttonLabel(i), 
            command=lambda i=i: self.play_song(i, app), bg=buttonColor(self.songs[i]), width=20, font=('Helvetica',20)).grid(column=i%2, row=int(i/2)+2)
        
    def play_song(self, index, app):
        self.songs[index].play(app, self)
    
    def play_random(self, app):
        incomplete = [song for song in self.songs if not song.completed]
        incomplete[rand.randint(0, len(incomplete)-1)].play(app, self)

    def __str__(self):
        return "self.name :".join(["\n"+str(s) for s in self.songs])

class AnimeApp:

    def __init__(self, difficulties):
        self.difficulties = difficulties
        self.root = Tk()
        self.root.config(bg="#101020")
        s = ttk.Style()
        s.configure('TButton', height=10, width=20, foreground="black")
        s.configure('TEntry', height=10, width=20, foreground="black")
        s.configure('.', font=('Helvetica', 20), background="#101020", foreground="white")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(columnspan=2)
        self.mainframe.config()

        self.root.geometry("1280x650")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.iconbitmap("anime_icon6621.ico")
        self.root.title("Anime Watchdle")

    def main_menu(self):
        self.clear_frame()
        ttk.Label(self.mainframe, text="Choose a Difficulty").grid(column=0, row=0)
        for i in range(len(self.difficulties)):
            ttk.Button(self.mainframe, text=self.difficulties[i].name, 
            command=lambda i=i: self.show_songs(i)).grid(column=0, row=i+1)

        self.root.mainloop()
    
    def clear_frame(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def show_songs(self, index):
        self.difficulties[index].display_difficulty(self)
    
    def __str__(self):
        return "".join([str(s)+"\n" for s in self.difficulties])

def load_app():
    difficulties = []
    for difficulty in os.listdir("songs"):
        songs = []
        dir = os.path.join("songs", difficulty)
        for song in os.listdir(dir):
            with open(os.path.join(dir, song)) as s:
                songs.append(Song(s, song))
        difficulties.append(SongDifficulty(songs, difficulty))
    return AnimeApp(difficulties)

if __name__ == '__main__':

    mainApp = load_app()

    mainApp.main_menu()
