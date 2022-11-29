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
ttk.Label(mainframe, textvariable=title).grid(column=0, row=2)

heard = StringVar()
heard.set("Heard : ")
heard_label = ttk.Label(mainframe, textvariable=heard)
heard_label.grid(column=0, row=4)

data = AnimeData()

cover_label = Label(mainframe)
cover_label.grid(column=0, row=1)

banner_label = Label(mainframe)
banner_label.grid(column=0, row=0)

def update_img():
    img = Image.open('cover_img.jpg')
    ratio = img.size[0]/img.size[1]
    img = img.resize((200, int(200/ratio)))
    img = ImageTk.PhotoImage(img)
    cover_label.configure(image=img)
    cover_label.image = img

    img = Image.open('banner_img.jpg')
    ratio = img.size[0]/img.size[1]
    img = img.resize((500, int(500/ratio)))
    img = ImageTk.PhotoImage(img)
    banner_label.configure(image = img)
    banner_label.image = img

def audio_fn():
    root.configure(bg="green")
    threshold = 4000
    res = get_audio(threshold)
    root.configure(bg="gray")
    heard.set(f"Heard : {res}")
    val = data.get_anime_data(res)
    if val != None:
        data.set_anime_image(res)
        update_img()
        title.set(f"{val['name_english']} / {val['name_romaji']}")
    else:
        title.set("Not found")
    
ttk.Button(mainframe, text="listen", command=audio_fn).grid(column=0, row=3)

root.mainloop()