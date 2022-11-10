from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url


class RegisterPageTest(BaseCase):

    def test_register_success(self, *_):
        """
        Testing R1-1 ~ R1-7
        Method: Output partition
        Analysis: If the output is a successful registration,
        then the inputs must all satisfy the requirments.
        """
        # delete this row if it already exists
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = path + "/../../qbay/data.db"
        print(db_path)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM Users WHERE email = (?)",
                       ("test0@test.com", ))
        row = cursor.fetchone()
        # test email exists
        if row is not None:
            print("------test email already exists------")
            cursor.execute("DELETE FROM Users WHERE email = (?)",
                           ("test0@test.com", ))
        connection.commit()
        connection.close()

        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0@test.com")
        self.send_keys("#name", "noname")
        self.send_keys("#first_name", "Huilin")
        self.send_keys("#last_name", "Xu")
        self.send_keys("#password", "Qwe456@")
        self.send_keys("#password2", "Qwe456@")

        # click enter button
        self.click('#reg-btn')

        # it checks if successful registration leads to the login page
        new_page_url = self.get_current_url()
        # print(new_page_url)
        self.assert_equal(new_page_url, base_url + '/login')

    def test_email_exists(self, *_):
        """
        Testing R1-7: If the email has been used, the operation failed.
        Method: Input partition
        Analysis: The input email either already exists in the db or not.
        Here I test the case where the email is in use, then registration
        should fail and an error msg should be displayed on the web page.
        """
        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0@test.com")
        self.type("#name", "noname")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "Qwe456@")
        self.type("#password2", "Qwe456@")

        # click enter button
        self.click('#reg-btn')

        # check if the error msg pops up on the page
        self.assert_text("Email has been used!", "#msg")

    def test_username_bound(self, *_):
        """
        Testing R1-6: User name has to be longer than 2 characters
        and less than 20 characters.
        Method: Input boundary testing
        Analysis: test boundary value 2 for username length, it should
        fails the registration.
        """
        # delete this row if it already exists
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = path + "/../../qbay/data.db"
        print(db_path)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM Users WHERE email = (?)",
                       ("test1@test.com", ))
        row = cursor.fetchone()
        # test email exists
        if row is not None:
            print("------test email already exists------")
            cursor.execute("DELETE FROM Users WHERE email = (?)",
                           ("test1@test.com", ))
        connection.commit()
        connection.close()

        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test1@test.com")
        self.type("#name", "aa")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "Qwe456@")
        self.type("#password2", "Qwe456@")

        # click enter button
        self.click('#reg-btn')

        self.assert_text(
            "User name has to be longer than 2 characters " +
            "and less than 20 characters.", "#msg")
