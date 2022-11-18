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
        # path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
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

    def test_password_empty(self, *_):
        """
        Testing R1-1: password cannot be empty.
        Method: Input partition
        Analysis: if the password field is empty,
        registration fails and won't go to login page.
        """
        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0@test.com")
        self.type("#name", "noname")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "")
        self.type("#password2", "")

        # click enter button
        self.click('#reg-btn')

        # it checks if unsuccessful registration does not go to the login page
        new_page_url = self.get_current_url()
        print(new_page_url)
        self.assert_equal(new_page_url, base_url + '/register')

    def test_unique_user(self, *_):
        """
        Testing R1-2: a user is uniquely identified by id.
        Method: Output partition
        Analysis: If the output is a unique user registration,
        then the inputs satisfy the requirments.
        After registration, the new user's id is unque in db.
        """
        # delete this row if it already exists
        # path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
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

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = (?)",
                       ("test0@test.com", ))
        row = cursor.fetchone()
        # print(row)
        id = row[0]

        cursor.execute("SELECT * FROM Users WHERE user_id = (?)",
                       (id, ))
        rows = cursor.fetchall()
        # print(rows)
        connection.close()

        # there is only one user with such id
        assert (len(rows) == 1)

    def test_email_wrong_pattern(self, *_):
        """
        Testing R1-3: email has to follow addr-spec in RFC 5322
        Method: Input partition
        Analysis: email either follow addr-spec or no,
        here is an test for an email that does not follow.
        Expected behaviour: fail to register
        """
        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0test.com")
        self.type("#name", "noname")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "")
        self.type("#password2", "")

        # click enter button
        self.click('#reg-btn')

        # it checks if unsuccessful registration does not go to the login page
        new_page_url = self.get_current_url()
        print(new_page_url)
        self.assert_equal(new_page_url, base_url + '/register')

    def test_password_complexity(self, *_):
        """
        Testing R1-4: Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower case,
        and at least one special character.
        Method: Input boundary testing
        Analysis: Here is a case where the password with length 5.
        It should fail the registration process.
        """
        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0@test.com")
        self.type("#name", "noname")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "Qwe")
        self.type("#password2", "Qwe")

        # click enter button
        self.click('#reg-btn')

        # check if the error msg pops up on the page
        self.assert_text("Password has to meet the required" +
                         " complexity: minimum length 6, at least" +
                         " one upper case,at least one lower case," +
                         " and at least one special character.", "#msg")

    def test_username_invalid(self, *_):
        """
        Testing R1-5: username has to be non-empty, alphanumeric-only,
        and space allowed only if it is not as the prefix or suffix.
        Method: Input partition
        Analysis: Here is a case where the username is not alphanumeric-only.
        """
        # open register page
        self.open(base_url + '/register')

        # fill all fields
        self.send_keys("#email", "test0@test.com")
        self.type("#name", "non*@%$^@(!")
        self.type("#first_name", "Huilin")
        self.type("#last_name", "Xu")
        self.type("#password", "Qwe123@")
        self.type("#password2", "Qwe123@")

        # click enter button
        self.click('#reg-btn')

        # check if the error msg pops up on the page
        self.assert_text("User name has to be non-empty, alphanumeric-only," +
                         " and space allowed only if it is not as the" +
                         " prefix or suffix.", "#msg")

    def test_username_bound(self, *_):
        """
        Testing R1-6: User name has to be longer than 2 characters
        and less than 20 characters.
        Method: Input boundary testing
        Analysis: test boundary value 2 for username length, it should
        fails the registration.
        """
        # delete this row if it already exists
        # path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.getcwd())
        db_path = path + "/qbay/data.db"
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

    def test_empty_address_and_postal_code(self, *_):
        """
        Testing R1-8, R1-9: address and postal code are
        empty at the time of registration.
        Method: Output partition
        Analysis: If the outputs are indeed empty,
        then the inputs satisfy requirments.
        """
        # delete this row if it already exists
        # path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
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

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = (?)",
                       ("test0@test.com", ))
        row = cursor.fetchone()
        address = row[9]
        postal_code = row[10]
        # print(row)
        connection.close()

        # there is only one user with such id
        assert (address is None and postal_code is None)

    def test_balance_is_100(self, *_):
        """
        Testing R1-10: Balance should be initialized
        as 100 at the time of registration.
        Method: Output partition
        Analysis: If the balance is indeed 100,
        then the inputs satisfy requirments.
        """
        # delete this row if it already exists
        # path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.getcwd())
        print(type(path))
        db_path = path + "/qbay/data.db"
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

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = (?)",
                       ("test0@test.com", ))
        row = cursor.fetchone()
        balance = row[6]
        # print(row)
        connection.close()

        # there is only one user with such id
        assert (balance == 100)
