from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url
from unittest.mock import patch

"""
This file defines user update tests for the frontend homepage.
"""


class Test(BaseCase):

    def test_update_listing_success(self, *_):
        """
        This is a test from login to user update page
        and verify if the tickets are correctly listed.
        """

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "111@111.com")
        # fill in user password
        self.type("#password", "123!Abc")
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        # test if element password exist
        self.assert_element("#password")
        # test if picture exist
        self.assert_element('img[alt="Nice pic"]')
        # fill in changed user name
        self.type("#name1", "Cloud")
        # fill in changed user postal code
        self.type("#Postal_Code", "K7K9M3")
        # hit the button to save change
        self.click("#btn-submit")


def test_is_name_changed():
    """
    This is a test to verify if the name really change
    """

    # link the database first
    path = os.path.abspath(os.getcwd())
    connection = sqlite3.connect(path + "/qbay/data.db")
    cursor = connection.cursor()

    # find name in the database according to user email
    cursor.execute("SELECT acc_name FROM Users WHERE email=?",
                   ("111@111.com",))
    (acc_name,) = cursor.fetchone()
    print(acc_name)

    connection.close()

    # if not equal, raise error
    if acc_name != "Cloud":
        raise Exception("name is not updated")


def test_is_postal_changed():
    """
    This is a test to verify if the postal code really change
    """
    path = os.path.abspath(os.getcwd())
    connection = sqlite3.connect(path + "/qbay/data.db")
    cursor = connection.cursor()

    # find postal code in the database according to user email
    cursor.execute("SELECT postal_code FROM Users WHERE email=?",
                   ("111@111.com",))
    (postal_code,) = cursor.fetchone()
    print(postal_code)

    connection.close()

    # if not equal, raise error
    if postal_code != "K7K9M3":
        raise Exception("Postal Code is not updated")
