import os
import tkinter
from PIL import Image, ImageTk
import random


def get_images_files():
    list_images = []
    list_extentions = [".jpg", ".jpeg", ".bmp", ".png"]
    dir_path = "images"
    for path in os.listdir(dir_path):
        file = os.path.join(dir_path, path)
        if os.path.isfile(file):
            _, ext = os.path.splitext(file)
            if ext in list_extentions:
                list_images.append(file)
    random.shuffle(list_images)
    return list_images


class AwardForm(tkinter.Tk):
    def __init__(self, parent_app):
        super(AwardForm, self).__init__()
        self.app = parent_app

        self.title("Reward image")
        form_width = min(self.winfo_screenwidth(), 800)
        form_height = min(self.winfo_screenheight(), 600)
        self.geometry(f"={form_width}x{form_height}+{(self.winfo_screenwidth() - form_width) // 2}+{(self.winfo_screenheight() - form_height) // 2 - 100}")
        self.resizable(False, False)
        self.overrideredirect(True)

        if not self.app.list_images:
            return

        image = Image.open(self.app.list_images.pop())
        # Изменить размер картинки под форму
        dw = image.width / form_width
        dh = image.height / form_height
        dmin = min(dw, dh)
        image = image.resize((int(image.width / dmin), int(image.height / dmin)), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image=image, master=self)

        self.canvas = tkinter.Canvas(self)
        self.canvas.create_image(form_width // 2, form_height // 2, image=photo, anchor=tkinter.CENTER)
        self.canvas.pack(expand=True, fill=tkinter.BOTH)

        self.bind('<Button-1>', self.close_window)
        self.bind('<Any-Key>', self.close_window)

        self.task_after = self.after(self.app.config.award_show_time, self.close_window, None)

        self.mainloop()

    def close_window(self, event):
        self.after_cancel(self.task_after)
        self.quit()
