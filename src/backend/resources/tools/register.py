"""
R1-1: Email cannot be empty. password cannot be empty.
R1-2: A user is uniquely identified by
        his/her user id - automatically generated.
R1-3: The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for
        a human-friendly explanation).
        You can use external libraries/imports.
R1-4: Password has to meet the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character.
R1-5: User name has to be non-empty, alphanumeric-only, and space
        allowed only if it is not as the prefix or suffix.
R1-6: User name has to be longer than 2 characters and less than 20 characters.
R1-7: If the email has been used, the operation failed.
R1-8: Shipping address is empty at the time of registration.
R1-9: Postal code is empty at the time of registration.
R1-10: Balance should be initialized as 100 at the time of registration.
       (free $100 dollar signup bonus).
"""

import json
import uuid
import re
import sqlite3


def register_format_checker(reg_user) -> None:
    print("===testing register format checker========")

    '''
    This function is used to do the format checking of the register
    data, the following rules will be checked:
            R1-1, R1-3, R1-4, R1-5, R1-6, R1-8, R1-9
    You can take look of the comment above to find out what is each if
    testing about
    '''

    # R1-1
    if ("email" not in reg_user or len(reg_user["email"]) == 0):
        raise InvaildRegister(
            "Email cannot be empty.", "Email-Zero")
    # R1-1
    if ("password" not in reg_user or len(reg_user["password"]) == 0):
        raise InvaildRegister(
            "password cannot be empty.", "password")
    # R1-8
    if ("address" in reg_user):
        raise InvaildRegister(
            "Shipping address is empty at the time of registration.",
            "address")
    # R1-9
    if ("postal_code" in reg_user):
        raise InvaildRegister(
            "Postal code is empty at the time of registration.",
            "address")
    # R1-3
    if (not re.fullmatch(emailReg, reg_user["email"])):
        raise InvaildRegister(
            "The email has to follow addr-spec" +
            " defined in RFC 5322(aaa@ccc.xxx) ",
            "Email-Format")
    # R1-4
    if (not re.fullmatch(passwordReg, reg_user["password"])):
        raise InvaildRegister(
            "Password has to meet the required complexity:" +
            " minimum length 6, at least one upper case," +
            "at least one lower case, and at least" +
            " one special character.", "Invalid-password")
    # R1-5 R1-6
    if (not len(reg_user["acc_name"]) > 2 and len(reg_user["acc_name"]) < 20):
        raise InvaildRegister(
            "User name has to be longer than "
            "2 characters and less than 20 characters.",
            "account-length")
    # R1-5
    if (not re.fullmatch(AccNameReg, reg_user["acc_name"])):
        raise InvaildRegister(
            "User name has to be non-empty, alphanumeric-only, " +
            "and space allowed only if it is not as the " +
            "prefix or suffix.", "account")

    print("ALL-pass")


def register_saving(reg_user) -> dict:
    '''
    R1-2
    R1-7
    R1-10
    R1-8
    R1-9
    '''
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/../../data.db")
    cursor = connection.cursor()

    # R1-7
    cursor.execute("SELECT email FROM Users WHERE email = (?)",
                   (reg_user["email"], ))
    rows = cursor.fetchone()
    connection.close()

    if (rows is not None):
        raise InvaildRegister("Email has been used!", "Email-used")

    # R1-2
    reg_user["user_id"] = uuid.uuid4().hex

    # R1-10
    reg_user["balance"] = 100

    # R1-8
    reg_user["address"] = None

    # R1-9
    reg_user["postal_code"] = None

    print(json.dumps(reg_user, indent=4))
    return reg_user


if __name__ == '__main__':

    from regexRepo import emailReg, AccNameReg, passwordReg
    from exceptions import InvaildRegister
    import os
    import sys
    path = os.path.abspath(os.getcwd())
    sys.path.append(path)
    from models import UserModel
    from db import db

    user = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "password": "Best_lawer123",
        "email": "JimmyMcgill@SGA.com",
        "profile_photo": "Jimmy_McGill_BCS_S3.png",
        "about": "Hi. I'm Saul Goodman. Did you know that you have rights?",
    }
    user2 = {
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM.com",
        "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!",
    }

    register_format_checker(user)
    register_format_checker(user2)

    try:
        saveble_user1 = register_saving(user)
        userM1 = UserModel(**saveble_user1)
        db.session.add(userM1)
        db.session.commit()
    except Exception:
        print("Data has stored inside!")

    try:
        saveble_user2 = register_saving(user2)
        userM2 = UserModel(**saveble_user2)
        db.session.add(userM2)
        db.session.commit()
    except Exception:
        print("Data has stored inside!")

# not equal to __main__
else:
    from .regexRepo import emailReg, AccNameReg, passwordReg
    from .exceptions import InvaildRegister
