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
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()

    # R1-7
    cursor.execute("SELECT email FROM Users WHERE email = (?)",
                   (reg_user["email"], ))
    rows = cursor.fetchone()
    connection.close()

    if (rows is not None):
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
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (saveble_user["user_id"],
                        saveble_user["acc_name"],
                        saveble_user["first_name"],
                        saveble_user["last_name"],
                        saveble_user["password"],
                        saveble_user["email"],
                        saveble_user["balance"],
                        saveble_user["profile_photo"],
                        saveble_user["about"],
                        saveble_user["address"],
                        saveble_user["postal_code"]))
        connection.commit()
        connection.close()
    except InvalidRegister:
        raise InvalidRegister("Registration failed:(", "fail to commit")


if __name__ == '__main__':

    from regexRepo import emailReg, AccNameReg, passwordReg
    from exceptions import InvalidRegister
    import os
    import sys
    path = os.path.abspath(os.getcwd())
    sys.path.append(path)

    user = {
        "acc_name": "Gisellesb",
        "first_name": "Dean",
        "last_name": "Wexler",
        "password": "Kim!!123321dsb",
        "email": "DimDim@HHM.com",
        # "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am stupid!",
    }

    register_format_checker(user)
    # register_format_checker(user2)

    try:
        saveble_user1 = register_saving(user)
        # reg_user = Users(**saveble_user1)
        print("hellllooooo")
        # db.session.add(userM1)
        # db.session.commit()
        # import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        print("here")
        cursor.execute("INSERT INTO Users \
        (user_id, acc_name, first_name, last_name, password, \
            email, balance, profile_photo, about, address, postal_code)\
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (saveble_user1["user_id"],
                        saveble_user1["acc_name"],
                        saveble_user1["first_name"],
                        saveble_user1["last_name"],
                        saveble_user1["password"],
                        saveble_user1["email"],
                        saveble_user1["balance"],
                        saveble_user1["profile_photo"],
                        saveble_user1["about"],
                        saveble_user1["address"],
                        saveble_user1["postal_code"]))
        print("before commit")
        connection.commit()
        print("commit complete")
        connection.close()
    except Exception:
        print("Data has stored inside!")

    # try:
    #     saveble_user2 = register_saving(user2)
    #     print("hellllooooo")
    #     userM2 = Users(**saveble_user2)
    #     print("show up plz")
    #     db.session.add(userM2)
    #     print("here?")
    #     db.session.commit()
    #     print("wtf!!!")
    # except Exception:
    #     print("Data has stored inside!")

# not equal to __main__
else:
    from qbay.regexRepo import emailReg, AccNameReg, \
        passwordReg, nameReg
    from qbay.exceptions import InvalidRegister
