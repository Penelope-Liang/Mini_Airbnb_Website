import pytest
import pathlib
from qbay.register import register_format_checker, \
    register_saving, register
import random
import os
import sqlite3

'''
This file test the sql injection against the register file
All of the injection code can't be email
but some of them can be account name, first name, and last name
And many of them can be password

The following program read in the injection code, and input the
them one by one, for every input, it only inject into one field
while other are remaining in correct format
'''

# read in all the injection lines to list
path = pathlib.Path(__file__)\
    .resolve().parent\
    .joinpath("Generic_SQLI.txt")
with open(path) as file:
    lines = [line.rstrip() for line in file]


def test_test_regsiter():

    for line in lines:

        random_int = random.randint(1, 1000)
        random_int2 = random.randint(1, 1000)
        random_string = str(random_int) + str(random_int2)

        injection_template = {
            "acc_name": "SaulGOODMAN" + random_string,
            "first_name": "Jimmy",
            "last_name": "McGill",
            "password": "I_loveKIM123!",
            "email": random_string + "JimmyBCS@BCS.com",
        }

        for key in injection_template:

            '''
            We select a key to be changed to injection
            code
            '''

            with pytest.raises(Exception):

                user = {**injection_template}
                user[key] = line

                # most of them raise format exception
                # from here
                register_format_checker(user)

                # some of them passed
                reg_user = register_saving(user)
                # register the new user to the database
                register(reg_user)

                # if pass, check if they in db or not
                path = os.path.\
                    abspath(os.getcwd())
                connection = sqlite3.connect(
                    path + "/qbay/data.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * \
                                FROM Users WHERE user_id = (?)",
                               (reg_user["user_id"],))
                row = cursor.fetchone()

                # if inside, delete it and help
                # to rasie an Exception to be true
                if row is not None:
                    cursor.execute("DELETE FROM \
                                   Users WHERE user_id = (?)",
                                   (reg_user["user_id"],))
                    connection.commit()
                    connection.close()
                    raise Exception("inject did not happen")

                # injection happen, as it expect an Expcetion
                # this is a false
                connection.commit()
                connection.close()
