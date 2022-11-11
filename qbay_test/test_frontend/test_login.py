from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url
from unittest.mock import patch


class LoginTest(BaseCase):

    def test_login_success(self, *_):
        """
        Testing R2-1 ~ R2-2
        Method: Output partition
        Analysis: If the output is a successful registration,
        then the inputs must all satisfy the requirements.
        """
        # login first
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "111@112.com")
        # fill in user password
        self.type("#password", "123!Abcc")
        # click login button to home page
        self.click("#btn-submit")

    def test_email_wrong_pattern(self, *_):
        """
        Testing R1-3: email has to follow addr-spec in RFC 5322
        Method: Input partition
        Analysis: email either follow addr-spec or no,
        here is an test for an email that does not follow.
        Expected behaviour: fail to register
        """
        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "111@112.com")
        # fill in user password
        self.type("#password", "123!Abcc")
        # click login button to home page
        self.click("#btn-submit")
        new_page_url = self.get_current_url()
        self.assert_equal(new_page_url, base_url + '/login')

    def test_password_complexity(self, *_):
        """
        Testing R1-4: Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower case,
        and at least one special character.
        Method: Input boundary testing
        Analysis: Here is a case where the password with length 5.
        It should fail the registration process.
        """

        self.open(base_url + "/login")
        # fill in user email
        self.type("#email", "111@112.com")
        # fill in user password
        self.type("#password", "11111")
        # click login button to home page
        self.click("#btn-submit")
        self.assert_text("Password has to meet the required" +
                         " complexity: minimum length 6, at least" +
                         " one upper case,at least one lower case," +
                         " and at least one special character.")
