class Person:
    def __init__(
        self,
        name,
        amount,
        founded,
        left,
        current_level,
        current_score,
        max_score_on_level,
    ):
        self.__name = name
        self.__amount = amount
        self.__founded = founded
        self.__left = left
        self.__current_level = current_level
        self.__current_score = current_score
        self.__max_score_on_level = max_score_on_level

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_founded(self):
        return self.__founded

    def get_left(self):
        return self.__left

    def get_current_level(self):
        return self.__current_level

    def get_current_score(self):
        return self.__current_score

    def get_max_score_on_level(self):
        return self.__max_score_on_level

    def set_name(self, name):
        self.__name = name

    def set_amount(self, amount):
        self.__amount = amount

    def set_founded(self, founded):
        self.__founded = founded

    def set_left(self, left):
        self.__left = left

    def set_current_level(self, current_level):
        self.__current_level = current_level

    def set_current_score(self, current_score):
        self.__current_score = current_score

    def set_max_score_on_level(self, max_score_on_level):
        self.__max_score_on_level = max_score_on_level
