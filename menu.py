from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from anime_database import AnimeData as db

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
        self.entry = ttk.Entry(app.mainframe)
        self.entry.grid(row=1, column=1)
        ttk.Button(app.mainframe, text="Enter", command = lambda:self.check_guess(app, prev)).grid(column=1, row=2)
        print(f"Now playing {self.name}")

    def check_guess(self, app, prev):
        entered = self.db.get_anime_data(self.entry.get())["name_english"]
        actual = self.db.get_anime_data(self.name)["name_english"]
        if entered == actual:
            self.completed=True
            self.back(app, prev)

    def back(self, app, prev):
        prev.display_difficulty(app)

    def __str__(self):
        return self.name

class SongDifficulty:

    def __init__(self, songs, name):
        self.songs = songs
        self.name = name

    def display_difficulty(self, app):
        app.clear_frame()
        ttk.Button(app.mainframe, text="Back", command = app.main_menu).grid(column=0, row=0)
        ttk.Label(app.mainframe, text="Select a song").grid(column=0, row=1)
        for i in range(len(self.songs)):
            buttonColor = lambda song: "light green" if song.completed else "light gray" if song.attempted else "white"
            tk.Button(app.mainframe, text=f"{self.songs[i].name}", 
            command=lambda i=i: self.play_song(i, app), bg=buttonColor(self.songs[i])).grid(column=0, row=i+2)
        
    def play_song(self, index, app):
        self.songs[index].play(app, self)
    
    def __str__(self):
        return "self.name :".join(["\n"+str(s) for s in self.songs])

class AnimeApp:

    def __init__(self, difficulties):
        self.difficulties = difficulties
        self.root = Tk()
        
        s = ttk.Style()
        s.configure("My.TFrame", bg="black", fg="white")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12", style="My.TFrame")
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
