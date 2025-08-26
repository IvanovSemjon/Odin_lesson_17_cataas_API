from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import Toplevel


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
    img = load_img(url)
    new_window = Toplevel(window)
    new_window.title("Картинка с котиком")
    new_window.geometry("600x480")
    lable = Label(new_window, image=img)
    lable.pack()
    lable.image = img
    
    if img:
        lable.config(image=img)
        lable.image = img


def exit():
    window.destroy()    


window = Tk()
window.title("Cats!")
window.geometry("600x520")


# update_button = Button(text="Обновить", command=set_image)
# update_button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Обновить", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


url = "https://cataas.com/cat"

open_new_window()

window.mainloop()
