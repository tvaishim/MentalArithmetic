import random

import question


class QuestTableDivision(question.Question):
    def __init__(self):
        super(QuestTableDivision, self).__init__()

        self.question_type = 6
        self.question_description = f"Таблица деления"

    def generate(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        mul = x * y

        self.question_text = f"{mul} : {x}"
        self.right_answer_text = str(y)
