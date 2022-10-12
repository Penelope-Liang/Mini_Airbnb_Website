'''
define you excpetions classes here
'''


class InvaildRegister(Exception):
    def __init__(self, message, case) -> None:
        self.message = message
        self.case = case

    def message(self) -> str:
        return self.message


class InvalidLogin(Exception):
    def __init__(self, message) -> None:
        self.message = message
        # self.case = case


class InvalidListing(Exception):
    def __init__(self, message) -> None:
        self.message = message
        
