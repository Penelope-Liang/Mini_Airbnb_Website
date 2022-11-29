"""
R2-1: A user can log in using her/his email address and the password.
R2-2: The login function should check if the supplied inputs meet the
same email/password requirements as above, before checking the database.
"""
import re
import sqlite3
from qbay.exceptions import InvalidLogin

'''
Disclaimer:
You dont need to use the functions I defined,
you can create you owe structure, but the following datatype
is the one you should use!
'''


def login_checker(login_user) -> None:
    print("===testing login format checker========")

    '''
    This function is used to do the format checking of the login
    data, the following rules will be checked:
            R2-2
    You can take look of the comment above to find out what is each if
    testing about
    '''
    # R2-2
    # Check email format
    if "email" not in login_user or len(login_user["email"]) == 0:
        raise InvalidLogin(
            "Email cannot be empty.", "Email-Zero")
    # R2-2
    # Check password format
    if "password" not in login_user or len(login_user["password"]) == 0:
        raise InvalidLogin(
            "password cannot be empty.", "password")
    # R2-2
    # Check email format
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                        login_user["email"]):
        raise InvalidLogin(
            "The email has to follow addr-spec" +
            " defined in RFC 5322(aaa@ccc.xxx) ",
            "Email-Format")
    # R2-2
    # Check password format
    if not re.fullmatch(
            (r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
             r"(?=.*[#@$!%*?&()_])[A-Za-z\d#@$!%*?&()_]{6,}$"),
            login_user["password"]):
        raise InvalidLogin(
            "Password has to meet the required complexity:" +
            " minimum length 6, at least one upper case," +
            "at least one lower case, and at least" +
            " one special character.", "Invalid-password")
    print("ALL-pass")


def login_saving(login_user) -> dict:
    """
    R2-1
    """
    # Connection with database
    print("===testing login saving checker========")
    import pathlib
    path = pathlib.Path().resolve()
    connection = sqlite3.connect(path.__str__() + "/data.db")
    cursor = connection.cursor()
    # R1-7
    # Select email from user, if found, fetch
    cursor.execute("SELECT email, password FROM 'Users' WHERE email = (?)",
                   (login_user["email"],))
    rows = cursor.fetchone()
    connection.close()

    # if not found, email is not exist
    if rows is None:
        raise InvalidLogin("Email is not exist")

    # if found, return it
    elif login_user["password"] == rows[1]:
        return rows
