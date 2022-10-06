
'''
R2-1: A user can log in using her/his email address and the password.
R2-2: The login function should check if the supplied inputs meet the same email/password requirements as above, before checking the database.
'''
import json
import uuid
import re
import sqlite3

'''
Disclaimer: 
You dont need to use the functions I defined,
you can create you owe structure, but the following datatype
is the one you should use!
'''


def login_format_test(user) -> None:
    '''
    check R2-1 here
    '''
    pass


def password_check(user) -> bool:
    '''
    check R2-2 here
    '''
    pass


if __name__ == "__main__":
    from regexRepo import *
    from exceptions import *
    user_login1 = {
        "email": "JimmyMcgill@SGA.com",
        "password": "Best_lawer123"
    }

    user_login2 = {
        "email": "KimKim@HHM.com",
        "password": "Kim$$123321"
    }

    # passed these data in
    login_format_test(user_login1)
    password_check(user_login1)

else:
    from .regexRepo import *
    from .exceptions import *
