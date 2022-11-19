import pytest
import pathlib
from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from qbay.register import register_format_checker
from unittest.mock import patch
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


class Security_Of_SQL_Injection_Tes(BaseCase):

    def test_test_regsiter(self, *_):
        for line in lines:

            random_int = random.randint(1, 1000)
            random_int2 = random.randint(1, 1000)
            random_string = str(random_int) + str(random_int2)

            right_register_format = {

                "#name": "SaulGOODMAN" + random_string,

                "#first_name": "Jimmy",

                "#last_name": "McGill",

                "#password": "I_loveKIM123!",

                "#email": random_string + "JimmyBCS@BCS.com",

            }

            for key1 in right_register_format:

                '''
                We select a key to be changed to injection
                code
                '''

                # open the register page
                self.open(base_url + "/register")

                # type the injection code
                self.type(key1, line)

                for key2, value in right_register_format.items():

                    '''
                    then for all other fields type the right format
                    input
                    '''
                    if key2 != key1:
                        self.type(key2, value)

                # the key1 is the password,
                # use line as the confirm password
                if key1 == "#password":
                    self.type("#password2", line)

                # or use the correct format data
                else:
                    self.type("#password2",
                              right_register_format["#password"])

                try:

                    '''
                    try to click the sumbmit bottom here
                    Nomarlly, as the format reason, most of the 
                    request will be block(also see below), but 
                    many of them 
                    '''
                    self.click("#reg-btn")

                    '''
                    Cases of the injection code pass the format checking
                    '''
                    if key1 != "#email":
                        try:

                            # make a JSON that contains the registration info
                            user = {
                                "acc_name":
                                    right_register_format["#name"],
                                "first_name":
                                    right_register_format["#first_name"],
                                "last_name":
                                    right_register_format["#last_name"],
                                "password":
                                    right_register_format["#password"],
                                "email":
                                    right_register_format["#email"],
                            }

                            # alter the line accordingly
                            if key1 == "#password":
                                user["password"] = line
                            elif key1 == "#first_name":
                                user["first_name"] = line
                            elif key1 == "#last_name":
                                user["last_name"] = line
                            elif key1 == "#name":
                                user["#name"] = line

                            # run the format checker again
                            register_format_checker(user)

                            # check the database with strict format,
                            # to see if the data correctly record
                            path = os.path.\
                                abspath(os.getcwd())
                            connection = sqlite3.connect(
                                path + "/qbay/data.db")
                            cursor = connection.cursor()
                            cursor.execute("SELECT * \
                                           FROM Users WHERE email=? \
                                           and acc_name=? \
                                           and first_name = ? \
                                           and last_name = ?\
                                           and password = ?",
                                           (user["email"],
                                            user["acc_name"],
                                            user["first_name"],
                                            user["last_name"],
                                            user["password"]))
                            row = cursor.fetchone()
                            connection.close()

                            # If data is not in there,
                            # this means the
                            if row is None:
                                '''
                                If can't find a exact record in the database
                                this means the injection might happend, and
                                there is hidden injection where the format
                                checker can't detect.
                                '''
                                raise Exception(
                                    "data are not in the database, \
                                    Injection might happened")

                            assert True

                        except Exception:

                            '''
                            cases of format checker did not pass
                            but the below exception did not trigger

                            or

                            can't find a exact record in the database

                            these are signs of injection might happen
                            somewhere else in the system
                            '''
                            assert False

                except Exception:

                    '''
                    Block by format checker, which prevents the injection
                    '''
                    assert True
