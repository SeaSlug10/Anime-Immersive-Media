from tkinter import *
from tkinter import ttk
from anime_database import AnimeData
from interact import get_audio
from PIL import ImageTk, Image

root = Tk()
root.title("Anime Immersion")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = StringVar()
title.set("anime title / japanese title")
ttk.Label(mainframe, textvariable=title).grid(column=0, row=1, sticky=(W))

heard = StringVar()
heard.set("Heard : ")
ttk.Label(mainframe, textvariable=heard).grid(column=1, row=2, sticky=(E))

data = AnimeData()

cover_label = Label(mainframe)
cover_label.grid(column=0, row=0, sticky=(E))

def update_img():
    img = Image.open('cover_img.jpg')
    img = ImageTk.PhotoImage(img)
    cover_label.configure(image=img)
    cover_label.image = img

def audio_fn():
    threshold = 3000
    res = get_audio(threshold)
    heard.set(f"Heard : {res}")
    val = data.get_anime_data(res)
    data.set_anime_image(res)
    update_img()
    title.set(f"{val['name_english']} / {val['name_romaji']}")

ttk.Button(mainframe, text="listen", command=audio_fn).grid(column=1, row=1, sticky=(W, E))

root.mainloop()