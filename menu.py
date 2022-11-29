from tkinter import *
from tkinter import ttk


class Song:

    def __init__(self, path):
        self.path = path

    def play(self):
        print(f"Now playing {self.path}")

class SongDifficulty:

    def __init__(self, songs, name):
        self.songs = songs
        self.name = name

    def display_difficulty(self, app):
        app.clear_frame()
        ttk.Button(app.mainframe, text="Back", command = app.main_menu).grid(column=0, row=0)
        ttk.Label(app.mainframe, text="Select a song").grid(column=0, row=1)
        for i in range(len(self.songs)):
            ttk.Button(app.mainframe, text=f"Song {i+1}", 
            command=lambda i=i: self.play_song(i)).grid(column=0, row=i+2)
        
    
    def play_song(self, index):
        self.songs[index].play()

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

    
if __name__ == '__main__':
    hard_songs = SongDifficulty([Song("this"), Song("that")], "hard")
    easy_songs = SongDifficulty([Song("the"), Song("other")], "easy")
    mainApp = AnimeApp([hard_songs, easy_songs])
    mainApp.main_menu()
