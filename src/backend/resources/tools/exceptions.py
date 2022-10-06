'''
define you excpetions classes here
'''
from ast import Str


class InvaildRegister(Exception):
    def __init__(self, message, case) -> None:
        self.message = message
        self.case = case

    def message(self) -> Str:
        return self.message


class InvalidLogin(Exception):
    def __init__(self, message) -> None:
        self.message = message
        # self.case = case
