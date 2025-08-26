from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


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


def set_image():
    img = load_img(url)
    if img:
        lable.config(image=img)
        lable.image = img


def exit():
    window.destroy()    

window = Tk()
window.title("Cats!")
window.geometry("600x520")


lable = Label()
lable.pack()

# update_button = Button(text="Обновить", command=set_image)
# update_button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Обновить", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)



url = "https://cataas.com/cat"

set_image()

window.mainloop()
