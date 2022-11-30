from datetime import date
from seleniumbase import BaseCase
import os
import sqlite3
import pytest
from qbay_test.conftest import base_url
from unittest.mock import patch

'''
A user cannot book a listing for his/her listing.
A user cannot book a listing that costs
    more than his/her balance.
A user cannot book a listing that is
    already booked with the overlapped dates.
A booked listing will show up on the
    user's home page (up-coming stages).
'''

path = os.path.abspath(os.getcwd())
connection = sqlite3.connect(path + "/qbay/data.db")
cursor = connection.cursor()
cursor.execute("SELECT email FROM Users WHERE user_id=?",
               ("b36524c626e64b15b3dcebb6d21dd5d8",))
(email,) = cursor.fetchone()
cursor.execute("SELECT password FROM Users WHERE user_id=?",
               ("b36524c626e64b15b3dcebb6d21dd5d8",))
(password,) = cursor.fetchone()
connection.close()


class Test(BaseCase):

    def test_book_success(self, *_):
        """
        Testing ALL
        Method: Output partition
        Analysis: If the output is a successful registration,
        then the inputs must all satisfy the requirements.
        """
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
        print(db_path)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Transactions WHERE property_id = (?)",
                       ("ebbc91cdf0f646e9993222418c39c69d", ))
        row = cursor.fetchone()
        # test email exists
        if row is not None:
            print("------test booking prop target already exists------")
            cursor.execute("DELETE FROM Transactions WHERE property_id = (?)",
                           ("ebbc91cdf0f646e9993222418c39c69d", ))
        else:
            print("------safe to proceed------")
        connection.commit()
        connection.close()

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click booking
        self.click("#booking")
        self.click("#ebbc91cdf0f646e9993222418c39c69d")
        self.type("#date", "2022-11-01")
        self.type("#date2", "2022-11-02")
        self.type("#guest_number", "1")
        self.click("#click2")

        # check if the booking succeeds and brings the user back to home page
        new_page_url = self.get_current_url()
        print(new_page_url)
        self.assert_equal(new_page_url, base_url + '/')

    def test_ownership_invalid(self, *_):
        """
        Testing : R6-1 A user cannot book a listing for his/her listing.
        Method: Input partition
        Analysis: Here is a case where the user book a list of herself.
        """

        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "171@yahoo.com")
        # fill in user password
        self.type("#password", "Yuan_yuan123")
        # click login button to home page
        self.click("#btn-submit")

        self.click("#booking")
        # print(self.get_text_content("#dfa708de23b541808202133f2dde7c58"))
        # print("im here SCROLLED!!")
        self.click("#ebbc91cdf0f646e9993222418c39c69d")
        self.type("#date", "2022-11-03")
        self.type("#date2", "2022-11-04")
        self.type("#guest_number", "1")
        self.click("#click2")
        # print(self.assert_element("#msg"))
        # print(self.get_text_content("#msg"))
        # print("^^^^")
        self.assert_text("User can't book his own property", "#msg")

    def test_balance_invalid(self, *_):
        """
        Testing : R6-2 A user cannot book a listing that costs
        more than his/her balance.
        Method: Input partition
        Analysis: Here is a case where the user attempt to book a
        list cost more than balance.
        """

        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "171@yahoo.com")
        # fill in user password
        self.type("#password", "Yuan_yuan123")
        # click login button to home page
        self.click("#btn-submit")

        self.click("#booking")
        self.scroll_to("#dfa708de23b541808202133f2dde7c58")
        # print("SCROLLED!!!!!!!!!!")
        self.click("#dfa708de23b541808202133f2dde7c58")
        self.type("#date", "2022-11-03")
        self.type("#date2", "2022-11-04")
        self.type("#guest_number", "1")
        self.click("#click2")
        # print(self.assert_element("#msg"))
        # print(self.get_text_content("#msg"))
        # print("^^^^")
        self.assert_text("User can't afford the property", "#msg")

    def test_overlapped_date(self, *_):
        """
        Testing : R6-3 A user cannot book a listing that is
        already booked with the overlapped dates.
        Method: Input partition
        Analysis: Here is a case where the user book a overlap date.
        """
        # delete the transaction im going to make first if it exists
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
        print(db_path)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Transactions WHERE property_id = (?)",
                       ("ebbc91cdf0f646e9993222418c39c69d", ))
        row = cursor.fetchone()
        # test email exists
        if row is not None:
            print("------test booking prop target already exists------")
            cursor.execute("DELETE FROM Transactions WHERE property_id = (?)",
                           ("ebbc91cdf0f646e9993222418c39c69d", ))
        else:
            print("------safe to proceed------")
        connection.commit()
        connection.close()

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click booking
        self.click("#booking")
        self.click("#ebbc91cdf0f646e9993222418c39c69d")
        self.type("#date", "2022-11-01")
        self.type("#date2", "2022-11-02")
        self.type("#guest_number", "1")
        self.click("#click2")

        # check if the booking succeeds and brings the user back to home page
        new_page_url = self.get_current_url()
        print(new_page_url)
        self.assert_equal(new_page_url, base_url + '/')
        self.click("#booking")
        self.click("#ebbc91cdf0f646e9993222418c39c69d")
        self.type("#date", "2022-11-01")
        self.type("#date2", "2022-11-02")
        self.type("#guest_number", "1")
        self.click("#click2")
        # print(self.assert_element("#msg"))
        # print(self.get_text_content("#msg"))
        # print("^^^^")
        self.assert_text("the selected date is overlapped", "#msg")
