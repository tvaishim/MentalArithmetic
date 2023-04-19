import random

import question


MAX_VALUE = 20


class QuestSubtraction20(question.Question):
    def __init__(self):
        super(QuestSubtraction20, self).__init__()

        self.question_type = 2
        self.question_description = f"Вычитание чисел до {MAX_VALUE}"

    def generate(self):
        sum = random.randint(2, MAX_VALUE)
        x = random.randint(1, sum - 1)
        y = sum - x

        self.question_text = f"{sum} - {x}"
        self.right_answer_text = str(y)
