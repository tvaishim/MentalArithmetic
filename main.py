import config
import logger
import questionform
import exam
import resultform
import awardform


class App:
    def __init__(self):
        self.log = logger.logger
        self.config = config.Config()

        self.list_images = awardform.get_images_files()

        self.exam = exam.Exam(exam_types=self.config.exam_types, max_questions=self.config.question_count)
        self.exam.start()

        self.log.info(f"-- Начало теста. Вопросов: {len(self.exam.list_exam_types)}")

        self.question_form = questionform.QuestionForm(self)
        self.question_form.destroy()

        self.result_form = resultform.ResultForm(self)
        self.result_form.destroy()

        self.log.info(f"-- Тест завершен\n{self.exam}\n")

    def show_award(self):
        award_form = awardform.AwardForm(self)
        award_form.destroy()


if __name__ == '__main__':
    app = App()
