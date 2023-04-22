import configparser

import logger


INI_FILE = r"config.ini"
SETT_FILE = r"sett.ini"


class Config:
    def __init__(self):
        self.data_config = configparser.ConfigParser(delimiters="=")
        self.data_setting = configparser.ConfigParser(delimiters="=")
        self.load_config()
        self.load_setting()
        self.questform_resized = False

        try:
            list_str = str(self.data_config['EXAM']['types']).split(",")
            self.exam_types = [int(item) for item in list_str]
        except Exception as e:
            self.exam_types = [5]
            logger.logger.error("Ошибка чтения файла настроек - параметр <[EXAM] types>")

        try:
            self.question_count = self.data_config.getint('EXAM', 'count')
        except Exception as e:
            self.exam_types = 10
            logger.logger.error("Ошибка чтения файла настроек - параметр <[EXAM] count>")

        try:
            self.show_right_answer = self.data_config.getboolean('SETTINGS', 'show_right_answer')
        except Exception as e:
            self.show_right_answer = True
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] show_right_answer>")

        try:
            self.right_answer_show_time = self.data_config.getint('SETTINGS', 'right_answer_show_time') * 1000
        except Exception as e:
            self.right_answer_show_time = 3000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] right_answer_show_time>")

        try:
            self.answer_color_time = self.data_config.getint('SETTINGS', 'answer_color_time') * 1000
        except Exception as e:
            self.answer_color_time = 1000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] answer_color_time>")

        try:
            self.show_award = self.data_config.getboolean('SETTINGS', 'show_award')
        except Exception as e:
            self.show_award = True
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] show_award>")

        try:
            self.quantity_quest_for_award = self.data_config.getint('SETTINGS', 'quantity_quest_for_award')
        except Exception as e:
            self.quantity_quest_for_award = 10
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] quantity_quest_for_award>")

        try:
            self.award_show_time = self.data_config.getint('SETTINGS', 'award_show_time') * 1000
        except Exception as e:
            self.award_show_time = 5000
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SETTINGS] award_show_time>")

        try:
            self.questform_width = self.data_setting.getint('QUESTFORM', 'width')
        except Exception as e:
            self.questform_width = 794
            logger.logger.error("Ошибка чтения файла параметров - параметр <[QUESTFORM] width>")

        try:
            self.questform_height = self.data_setting.getint('QUESTFORM', 'height')
        except Exception as e:
            self.questform_height = 540
            logger.logger.error("Ошибка чтения файла параметров - параметр <[QUESTFORM] height>")

    def load_config(self):
        self.data_config.read(INI_FILE)

    def load_setting(self):
        self.data_setting.read(SETT_FILE)

    def save_setting(self):
        if self.questform_resized:
            self.data_setting['QUESTFORM'] = {
                'width': str(self.questform_width),
                'height': str(self.questform_height)
            }
            with open(SETT_FILE, 'w') as settfile:
                self.data_setting.write(settfile)

