from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url
from unittest.mock import patch

import random

'''
using random int as string to make sure each
time testing using different value
'''
random_string = str(random.randint(1, 1000))
changed_name = "Los Pollos Hermanos " + random_string
changed_descri = "welcome to Los Pollos Hermanos, I am Gus Fring, \
                  we don't welcome Salamanca " + random_string


class FrontEndHomePageTest(BaseCase):

    def test_update_listing_success(self, *_):

        # login first
        self.open(base_url + "/login")
        self.type("#email", "111@111.com")
        self.type("#password", "123!Abc")
        self.click("#btn-submit")

        # click into properities editing GUI
        self.click("#edit-pro")
        self.click(
            "a[href='/updatelisting?"
            +
            "prop_id=5f1f29182d7e47b094e9f932ef19a976']")

        # start editing

        self.type("#title", changed_name)
        self.type("#description", changed_descri)
        self.click("#submit")

        self.click("#btn-submit")


def test_is_title_changed():

    path = os.path.abspath(os.getcwd())
    connection = sqlite3.connect(path + "/qbay/data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title FROM Properties WHERE prop_id=?",
                   ("5f1f29182d7e47b094e9f932ef19a976",))
    (title,) = cursor.fetchone()
    print(title)

    connection.close()
    if (title != changed_name):
        raise Exception("title is not updated")


def test_is_description_changed():

    path = os.path.abspath(os.getcwd())
    connection = sqlite3.connect(path + "/qbay/data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT description FROM Properties WHERE prop_id=?",
                   ("5f1f29182d7e47b094e9f932ef19a976",))
    (description,) = cursor.fetchone()
    print(description)

    connection.close()
    if (description != changed_descri):
        raise Exception("description is not updated")
