import random

import question


MAX_VALUE = 100


class QuestSubtraction100(question.Question):
    def __init__(self):
        super(QuestSubtraction100, self).__init__()

        self.question_type = 4
        self.question_description = f"Вычитание чисел до {MAX_VALUE}"

    def generate(self):
        sum = random.randint(25, MAX_VALUE)
        x = random.randint(1, sum - 1)
        y = sum - x

        self.question_text = f"{sum} - {x}"
        self.right_answer_text = str(y)
