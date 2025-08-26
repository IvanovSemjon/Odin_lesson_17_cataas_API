from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import Toplevel


Allowed_tags = [
    "sleep",
    "jump",
    "fight",
    "black",
    "white",
    "siamese",
    "cute",
    "play",
    ]


def load_img(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка --> {e}")
        return None


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_img(url_tag)
    if img:
        new_window = Toplevel(window)
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        lable = Label(new_window, image=img)
        lable.pack()
        lable.image = img
    

def exit():
    window.destroy()    


window = Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Обновить", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat"

tag_lable = Label(text="Выбери тег")
tag_lable.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()
