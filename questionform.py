import tkinter

import exam


class QuestionForm(tkinter.Tk):
    def __init__(self, parent_app):
        super(QuestionForm, self).__init__()
        self.app = parent_app

        self.question_text = ""
        self.answer_text = ""
        self.counter_for_award = 0

        self.title("Mental arithmetic")
        width = 794
        height = 540
        self.geometry(f"={width}x{height}+{(self.winfo_screenwidth() - width) // 2}+{(self.winfo_screenheight() - height) // 2 - 100}")
        # self.geometry('794x540+300+200')
        self.resizable(False, False)

        self.label0 = tkinter.Label(self, borderwidth=1, relief='sunken', font='arial 14')
        self.label0.place(x=5, y=5, width=784, height=30)

        self.label5 = tkinter.Label(self, text='Время', borderwidth=1, relief='sunken', foreground='Black')
        self.label5.place(x=5, y=40, width=192, height=30)

        self.label1 = tkinter.Label(self, text='Время', borderwidth=1, relief='sunken', foreground='Blue')
        self.label1.place(x=202, y=40, width=192, height=30)

        self.label2 = tkinter.Label(self, text='Слов', borderwidth=1, relief='sunken', foreground='Green')
        self.label2.place(x=399, y=40, width=192, height=30)

        self.label3 = tkinter.Label(self, text='Результат', borderwidth=1, relief='sunken', foreground='Red')
        self.label3.place(x=596, y=40, width=192, height=30)

        self.label4 = tkinter.Label(self, text='Вопрос', borderwidth=1, font='arial 60')
        self.label4.place(x=5, y=190, width=784, height=120)

        self.protocol('WM_DELETE_WINDOW', self.window_deleted)
        self.bind('<Key>', self.event_press_key)
        self.bind('<Return>', self.event_press_enter)
        self.bind('<BackSpace>', self.event_press_backspace)

        self.show_question()
        self.mainloop()

    def show_question(self):
        self.app.exam.do_question()
        if self.app.exam.status == exam.ExamStatus.finished:
            self.finish()
        self.question_text = self.app.exam.question.question_text
        self.answer_text = ""
        self.repaint_label()

    def repaint_label(self):
        answer_text = self.answer_text
        if not answer_text:
            answer_text = "?"
        self.label4.config(
            bg='SystemButtonFace',
            text=f"{self.question_text} = {answer_text}"
        )
        self.label0.config(text=f"{self.app.exam.question.question_description}")
        self.label5.config(text=f"{self.app.exam.counter_questions}")
        self.label1.config(text=f"{self.app.exam.counter_answers}")
        self.label2.config(text=f"{self.app.exam.counter_right}")
        self.label3.config(text=f"{self.app.exam.counter_wrong}")

    def window_deleted(self):
        self.close_window()

    def event_press_key(self, event):
        if not self.app.exam.question.char_valid(event.char):
            return
        str = self.answer_text + event.char
        if not self.app.exam.question.str_valid(str):
            return
        self.answer_text = str
        self.repaint_label()

    def event_press_enter(self, event):
        if self.answer_text:
            result_answer = self.app.exam.do_answer(self.answer_text)
            if result_answer:
                self.label4.config(bg='Green')
                self.label4.update()
                self.after(self.app.config.answer_color_time)
                self.counter_for_award += 1
                if self.app.config.show_award:
                    if self.counter_for_award % self.app.config.quantity_quest_for_award == 0:
                        self.app.show_award()
                self.show_question()
            else:
                self.app.log.info(f" -- Ошибка: {self.question_text} = {self.answer_text}")
                self.label4.config(bg='Red')
                self.label4.update()
                self.after(self.app.config.answer_color_time)
                if self.app.config.show_right_answer:
                    self.label4.config(
                        bg='Gold',
                        text=f"{self.question_text} = {self.app.exam.question.right_answer_text}"
                    )
                    self.label4.update()
                    self.after(self.app.config.right_answer_show_time)
                self.show_question()

    def event_press_backspace(self, event):
        self.answer_text = ""
        self.repaint_label()

    def finish(self):
        self.close_window()

    def close_window(self):
        self.quit()
        # self.destroy()
