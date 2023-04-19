import time
import enum
import random
from copy import copy

import question
import quest_addition_20
import quest_subtraction_20
import quest_addition_100
import quest_subtraction_100
import quest_table_multiplication
import quest_table_division


REPEAT_WRONG_QUESTIONS = True


class ExamStatus(enum.Enum):
    new = 0
    run = 1
    finished = 2


class Exam:
    def __init__(self, exam_types=None, max_questions=10, repeat=False):
        if exam_types is None:
            exam_types = [1]
        self.list_exam_types = exam_types * max_questions
        random.shuffle(self.list_exam_types)
        self.time_begin = 0
        self.time_end = 0
        self.counter_questions = len(self.list_exam_types)
        self.counter_answers = 0
        self.counter_right = 0
        self.counter_wrong = 0
        self.status = ExamStatus.new
        self.list_questions = []
        self.dim_failures = set()
        self.question = None
        self.can_repeat = repeat

    @staticmethod
    def create_question(question_type):
        match question_type:
            case 1:
                return quest_addition_20.QuestAddition20()
            case 2:
                return quest_subtraction_20.QuestSubtraction20()
            case 3:
                return quest_addition_100.QuestAddition100()
            case 4:
                return quest_subtraction_100.QuestSubtraction100()
            case 5:
                return quest_table_multiplication.QuestTableMultiplication()
            case 6:
                return quest_table_division.QuestTableDivision()
        return None

    def start(self):
        self.time_begin = time.time()
        self.time_end = 0
        self.counter_answers = 0
        self.counter_right = 0
        self.counter_wrong = 0
        self.status = ExamStatus.run

    def do_question(self):
        if self.list_exam_types:
            question_type = self.list_exam_types.pop()
            if self.can_repeat:
                self.question = self.create_question(question_type)
            else:
                for i in range(50):     # Ограничить цикл, на случай если примеров будет больше чем вариантов
                    self.question = self.create_question(question_type)
                    if self.question not in self.list_questions:
                        break

        else:
            if self.dim_failures:
                self.question = self.dim_failures.pop()
            else:
                self.status = ExamStatus.finished

    def do_answer(self, answer):
        self.counter_answers += 1
        result_answer = self.question.check(answer)
        self.list_questions.append(self.question)
        if result_answer:
            self.counter_right += 1
        else:
            self.counter_wrong += 1
            if REPEAT_WRONG_QUESTIONS:
                self.dim_failures.add(copy(self.question))
        return result_answer

    def get_result(self):
        if REPEAT_WRONG_QUESTIONS:
            percent = (self.counter_right-self.counter_wrong) * 100 // self.counter_questions
        else:
            percent = self.counter_right * 100 // self.counter_questions
        grade = round(percent / 20)
        if grade < 1:
            grade = 1
        return {
            "total": self.counter_questions,
            "count": self.counter_answers,
            "fail": self.counter_wrong,
            "percent": percent,
            "grade": grade,
        }

    def __repr__(self):
        result = self.get_result()
        return f"Всего заданий: {result['total']}\nВыполнено: {result['count']}\nОшибок: {result['fail']}\nРезультат: {result['percent']}%\nОценка: {result['grade']}"
