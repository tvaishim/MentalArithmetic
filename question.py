class Question:
    def __init__(self):
        self.question_type = 0
        self.question_description = ""
        self.question_text = ""
        self.answer_text = ""
        self.right_answer_text = ""
        self.valide_chars = "0123456789"
        self.valide_len = 5
        self.generate()

    def generate(self):
        self.question_text = "2+2"
        self.right_answer_text = "4"

    def check(self, answer):
        self.answer_text = answer
        return self.right_answer_text == answer

    def char_valid(self, char):
        return char in self.valide_chars

    def str_valid(self, str):
        if len(str) > self.valide_len:
            return False
        return True

    def __eq__(self, other):
        if not isinstance(other, Question):
            return False
        return self.question_type == other.question_type and self.question_text == other.question_text

    def __hash__(self):
        return hash(f"{str(self.question_type)}:{self.question_text}")

    def __repr__(self):
        return f"{self.question_text} = {self.answer_text}"

    def __copy__(self):
        new_copy = type(self)()
        new_copy.__dict__.update(self.__dict__)
        return new_copy

    def get_description(self):
        return self.question_description

