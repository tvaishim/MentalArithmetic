import tkinter


class ResultForm(tkinter.Tk):
    def __init__(self, parent_app):
        super(ResultForm, self).__init__()
        self.app = parent_app

        self.title("Test results")
        width = 400
        height = 300
        self.geometry(f"={width}x{height}+{(self.winfo_screenwidth() - width) // 2}+{(self.winfo_screenheight() - height) // 2 - 100}")
        self.resizable(False, False)

        self.label1 = tkinter.Label(self, font='arial 15')
        self.label1.place(x=0, y=0, relwidth=1, height=225)

        self.button1 = tkinter.Button(self, text='OK', command=self.close_window)
        self.button1.place(x=150, y=230, width=100, height=40)

        self.protocol('WM_DELETE_WINDOW', self.window_deleted)

        self.show_result()
        self.mainloop()

    def show_result(self):
        self.label1.config(text=str(self.app.exam))

    def window_deleted(self):
        self.close_window()

    def close_window(self):
        self.quit()
