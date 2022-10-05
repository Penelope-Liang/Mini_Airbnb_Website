'''
R1-1: Email cannot be empty. password cannot be empty.
R1-2: A user is uniquely identified by his/her user id - automatically generated.
R1-3: The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation). You can use external libraries/imports.
R1-4: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.
R1-5: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
R1-6: User name has to be longer than 2 characters and less than 20 characters.
R1-7: If the email has been used, the operation failed.
# R1-8: Shipping address is empty at the time of registration.
# R1-9: Postal code is empty at the time of registration.
R1-10: Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
'''

import json
import uuid
import re
import sqlite3
from multiprocessing import connection

# if __name__ != "__main__":
#     from .regexRepo import emailReg, AccNameReg, passwordReg
#     from .exceptions import InvaildRegister


def register_format_checker(reg_user):
    print("===testing register format checker========")

    '''
     R1-1
     R1-3
     R1-4
     R1-5 
     R1-6 
    '''

    # R1-1
    if (len(reg_user["email"]) == 0):
        print("Invalid email or password, shorter than zero")
        raise InvaildRegister(
            "Invalid email shorter than zero", "Email")
    if (len(reg_user["password"]) == 0):
        raise InvaildRegister(
            "Invalid password shorter than zero", "password")
    # R1-3
    if (not re.fullmatch(emailReg, reg_user["email"])):
        print("Invalid email")
        raise InvaildRegister(
            "Invalid email doesn't match the format", "Email-Format")
    # R1-4
    if (not re.fullmatch(passwordReg, reg_user["password"])):
        print("Invalid password")
        raise InvaildRegister(
            "[Invalid password] password doesn't match format", "Invalid-password")
    # R1-5 R1-6
    if (not len(reg_user["acc_name"]) > 2 and len(reg_user["acc_name"]) < 20):
        print("Invalid email")
        raise InvaildRegister(
            "Invalid length of account name used", "account-length")
    # R1-5
    if (not re.fullmatch(AccNameReg, reg_user["acc_name"])):
        print("Invalid account name")
        raise InvaildRegister(
            "Invalid account name used", "account")

    print("ALL-pass")


def register_saving(reg_user):
    '''
    R1-2
    R1-7
    R1-10
    '''
    connection = sqlite3.connect('./data.db')
    cursor = connection.cursor()

    # R1-7
    cursor.execute("SELECT email FROM Users WHERE email = (?)",
                   (reg_user["email"], ))
    rows = cursor.fetchone()
    connection.close()

    if (rows != None):
        print("Email Exisit!")
        raise InvaildRegister("Email has been used!", "Email-used")

    reg_user["user_id"] = uuid.uuid4().hex
    reg_user["balance"] = 100

    print(json.dumps(reg_user, indent=4))
    return reg_user


if __name__ == '__main__':

    from regexRepo import *
    from exceptions import *

    user = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "password": "Best_lawer123",
        "email": "JimmyMcgill@SGA.com",
        "profile_photo": "https://en.wikipedia.org/wiki/Saul_Goodman#/media/File:Jimmy_McGill_BCS_S3.png",
        "about": "Hi. I'm Saul Goodman. Did you know that you have rights?"
    }
    user2 = {
        # "user_id": None,
        # "review_id": None,(delete)
        # "tsc_id": None,(delete)
        # "property_id": None,(delete)
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM.com",
        # "balance": 0,
        "profile_photo": "https://en.wikipedia.org/wiki/Kim_Wexler#/media/File:Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!"
    }

    register_format_checker(user)
    register_format_checker(user2)
    register_saving(user)
    register_saving(user2)

# not equal to __main__
else:
    from .regexRepo import emailReg, AccNameReg, passwordReg
    from .exceptions import InvaildRegister
