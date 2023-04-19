import random

import question


MAX_VALUE = 20


class QuestAddition20(question.Question):
    def __init__(self):
        super(QuestAddition20, self).__init__()

        self.question_type = 1
        self.question_description = f"Сложение чисел до {MAX_VALUE}"

    def generate(self):
        sum = random.randint(2, MAX_VALUE)
        x = random.randint(1, sum - 1)
        y = sum - x

        self.question_text = f"{x} + {y}"
        self.right_answer_text = str(sum)
