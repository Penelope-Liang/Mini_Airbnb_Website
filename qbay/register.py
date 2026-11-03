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
from qbay.db import db
from qbay.models import Users
from qbay.regexRepo import emailReg, AccNameReg, passwordReg
from qbay.exceptions import InvalidRegister


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
    if "email" not in reg_user or len(reg_user["email"]) == 0:
        raise InvalidRegister(
            "Email cannot be empty.", "Email-Zero")
    # R1-1
    if ("password" not in reg_user or len(reg_user["password"]) == 0):
        raise InvalidRegister(
            "password cannot be empty.", "password")
    # R1-8
    if ("address" in reg_user):
        raise InvalidRegister(
            "Shipping address is empty at the time of registration.",
            "address")
    # R1-9
    if ("postal_code" in reg_user):
        raise InvalidRegister(
            "Postal code is empty at the time of registration.",
            "address")
    # R1-3
    if (not re.fullmatch(emailReg, reg_user["email"])):
        raise InvalidRegister(
            "The email has to follow addr-spec" +
            " defined in RFC 5322(aaa@ccc.xxx) ",
            "Email-Format")
    # R1-4
    if (not re.fullmatch(passwordReg, reg_user["password"])):
        print(reg_user["password"])
        print(not re.fullmatch(passwordReg, reg_user["password"]))
        raise InvalidRegister(
            "Password has to meet the required complexity:" +
            " minimum length 6, at least one upper case," +
            "at least one lower case, and at least" +
            " one special character.", "Invalid-password")
    # R1-5 R1-6
    if (not len(reg_user["acc_name"]) > 2 and len(reg_user["acc_name"]) < 20):
        raise InvalidRegister(
            "User name has to be longer than "
            "2 characters and less than 20 characters.",
            "account-length")
    # R1-5
    if (not re.fullmatch(AccNameReg, reg_user["acc_name"])):
        raise InvalidRegister(
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
    # R1-7
    if Users.query.filter_by(email=reg_user["email"]).first() is not None:
        raise InvalidRegister("Email has been used!", "Email-used")

    # R1-2
    reg_user["user_id"] = uuid.uuid4().hex

    # R1-10
    reg_user["balance"] = 100

    # R1-8
    reg_user["address"] = None

    # R1-9
    reg_user["postal_code"] = None

    if "profile_photo" not in reg_user:
        reg_user["profile_photo"] = None
    if "about" not in reg_user:
        reg_user["about"] = None
    # reg_user["profile_photo"] = None
    # reg_user["about"] = None

    print(json.dumps(reg_user, indent=4))
    return reg_user


def register(saveble_user):
    try:
        db.session.add(Users(**saveble_user))
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise InvalidRegister("Registration failed:(", "fail to commit")
