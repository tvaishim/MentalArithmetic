import random

import question


class QuestTableMultiplication(question.Question):
    def __init__(self):
        super(QuestTableMultiplication, self).__init__()

        self.question_type = 5
        self.question_description = f"Таблица умножения"

    def generate(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        mul = x * y

        self.question_text = f"{x} * {y}"
        self.right_answer_text = str(mul)
