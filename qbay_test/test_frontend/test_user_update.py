from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url
from unittest.mock import patch

"""
This file defines user update tests for the frontend homepage.
"""

path = os.path.abspath(os.getcwd())
connection = sqlite3.connect(path + "/qbay/data.db")
cursor = connection.cursor()
cursor.execute("SELECT email FROM Users WHERE user_id=?",
               ("98f8b57781864640a76fca66627b6206",))
(email,) = cursor.fetchone()
cursor.execute("SELECT password FROM Users WHERE user_id=?",
               ("98f8b57781864640a76fca66627b6206",))
(password,) = cursor.fetchone()
connection.close()


class Test(BaseCase):

    def test_update_listing_success(self, *_):
        """
        Testing R3-1 ~ R3-4
        Method: Output partition
        Analysis: If the output is a successful registration,
        then the inputs must all satisfy the requirements.
        """
        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
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
        self.type("#password", "Asd1231@")
        self.type("#email", "xiaomm@icloud.com")
        self.type("#Postal_Code", "K7K9M3")
        self.type("#billing_address", "666 Prices St")
        # hit the button to save change
        self.click("#btn-submit")

    def test_email_wrong_pattern(self, *_):
        """
        Testing R1-3: email has to follow addr-spec in RFC 5322
        Method: Input partition
        Analysis: email either follow addr-spec or no,
        here is an test for an email that does not follow.
        Expected behaviour: fail to register
        """
        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#email", "xiaommicloud.com")
        self.click("#btn-submit")
        new_page_url = self.get_current_url()
        self.assert_equal(new_page_url, base_url + '/update_user_save')

    def test_password_complexity(self, *_):
        """
        Testing R1-4: Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower case,
        and at least one special character.
        Method: Input boundary testing
        Analysis: Here is a case where the password with length 5.
        It should fail the registration process.
        """
        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#password", "11111")
        self.click("#btn-submit")
        self.assert_text("Password has to meet the required" +
                         " complexity: minimum length 6, at least" +
                         " one upper case,at least one lower case," +
                         " and at least one special character.")

    def test_username_invalid(self, *_):
        """
        Testing R3-4: username has to be non-empty, alphanumeric-only,
        and space allowed only if it is not as the prefix or suffix.
        Method: Input partition
        Analysis: Here is a case where the username is not alphanumeric-only.
        """

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#name1", "non*@%$^@(!")
        self.click("#btn-submit")
        self.assert_text("User name has to be non-empty, alphanumeric-only," +
                         " and space allowed only if it is not as the" +
                         " prefix or suffix.")

    def test_username_bound(self, *_):
        """
        Testing R3-4: User name has to be longer than 2 characters
        and less than 20 characters.
        Method: Input boundary testing
        Analysis: test boundary value 2 for username length, it should
        fails the registration.
        """

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#name1", "ii")
        self.click("#btn-submit")
        self.assert_text(
            "User name has to be longer than 2 characters " +
            "and less than 20 characters.")

    def test_postal_code_Invaild(self, *_):
        """
        Testing R3-2: postal code should be non-empty,
        alphanumeric-only, and no special characters such as !.
        Method: Input Input partition
        Analysis: Testing where postal code
        is not alphanumeric-only and contain !
        """

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#Postal_Code", "1111!1")
        self.click("#btn-submit")
        self.assert_text("Postal code has to meet the required complexity:" +
                         "non-empty, alphanumeric-only," +
                         "has to be a valid Canadian postal code")

    def test_postal_code_Invaild2(self, *_):
        """
        Testing R3-3: postal code should be non-empty,
        alphanumeric-only, and no special characters such as !.
        Method: Input Input partition
        Analysis: Testing where postal code
        is not alphanumeric-only and contain !
        """

        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", email)
        # fill in user password
        self.type("#password", password)
        # click login button to home page
        self.click("#btn-submit")

        # click update button to user update page
        self.click("#updates")

        # click update button to change info
        self.click("#btn-submit")
        self.type("#Postal_Code", "KKKK899I")
        self.click("#btn-submit")
        self.assert_text("Postal code has to meet the required complexity:" +
                         "non-empty, alphanumeric-only," +
                         "has to be a valid Canadian postal code")
