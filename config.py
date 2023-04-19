import configparser

import logger


INI_FILE = r"config.ini"


class Config:
    def __init__(self):
        self.data = None
        self.load_config()

        try:
            list_str = str(self.data['EXAM']['types']).split(",")
            self.exam_types = [int(item) for item in list_str]
        except Exception as e:
            self.exam_types = [5]
            logger.logger.error("Ошибка чтения файла настроек - параметр <[EXAM] types>")

        try:
            self.question_count = int(self.data['EXAM']['count'])
        except Exception as e:
            self.exam_types = 10
            logger.logger.error("Ошибка чтения файла настроек - параметр <[EXAM] count>")

        try:
            self.show_right_answer = bool(self.data['SETTINGS']['show_right_answer'])
        except Exception as e:
            self.show_right_answer = True
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] show_right_answer>")

        try:
            self.right_answer_show_time = int(self.data['SETTINGS']['right_answer_show_time']) * 1000
        except Exception as e:
            self.right_answer_show_time = 3000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] right_answer_show_time>")

        try:
            self.answer_color_time = int(self.data['SETTINGS']['answer_color_time']) * 1000
        except Exception as e:
            self.answer_color_time = 1000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] answer_color_time>")

        try:
            self.show_award = bool(self.data['SETTINGS']['show_award'])
        except Exception as e:
            self.show_award = True
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] show_award>")

        try:
            self.quantity_quest_for_award = int(self.data['SETTINGS']['quantity_quest_for_award'])
        except Exception as e:
            self.quantity_quest_for_award = 10
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] quantity_quest_for_award>")

        try:
            self.award_show_time = int(self.data['SETTINGS']['award_show_time']) * 1000
        except Exception as e:
            self.award_show_time = 5000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] award_show_time>")

    def load_config(self):
        self.data = configparser.ConfigParser(delimiters="=")
        self.data.read(INI_FILE)
