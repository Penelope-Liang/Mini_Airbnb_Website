from datetime import date
from seleniumbase import BaseCase
import os
import sqlite3
import pytest
from qbay_test.conftest import base_url
from unittest.mock import patch

"""
This file defines create listing test for the frontend homepage.
"""


class FrontEndHomePageTes(BaseCase):

    def test_createlisting_success(self, *_):
        """
        Testing R4-1 ~ R4-8
        Method: Output partition
        Analysis: If the output successfully creates,
        then the inputs must all satisfy the requirments.
        """
        # log in first
        self.open(base_url + "/login")
        self.type("#email", "111@111.com")
        self.type("#password", "123!Abc")
        self.click("#btn-submit")
        self.click("a[href='/create'")
        # create listing title
        self.type("#posted_date", date.today())
        self.type("#title", "Good place")
        # create listing description
        self.type("#description", "This is a nice place to live near lake")
        # self.input("#img", "1.png")
        # create listing price
        self.type("#price", 1000)
        # create listing address
        self.type("#address", "333 Horton Street")
        # create listing capacity
        self.type("#capacity", 10)
        # hit the button to save
        self.click("#submit")
    
    def test_create_title_with_unalphanumeric(self, *_):
        '''
        Testing R4-1: The title of the product has to be alphanumeric-only,
        and space allowed only if it is not as prefix and suffix.
        Method: Input partition
        Analysis: title either follow alphanumeric-only or no,
        and space allowed only if it is not as prefix and suffix.
        here is an test for an email that does not follow.
        Expected behaviour: fail to create
        '''

        with pytest.raises(Exception):
            # log in first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", "??/ds.;a")
            self.type("#description", "This is a nice place to live near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 100)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")

    def test_create_title_over_80(self, *_):

        '''
        Testing R4-2: The title of the product is no 
        longer than 80 characters.
        Analysis: Here is a case where the title over 80 characters.
        Method: Input boundary testing
        Analysis: Here is a case where the description is over 80 characters.
        It should fail the creating process.
        '''

        with pytest.raises(Exception):
            # log in first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", ''.join(["b"] * 100))
            self.type("#description", "This is a nice place to live near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 100)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            # self.click("#submit")
            self.click("#btn-submit")

    def test_create_description_length_less_20(self, *_):
        '''
        Testing R4-3: The description of the product can 
        be arbitrary characters, 
        with a minimum length of 20 characters
        Method: Input boundary testing
        Analysis: Here is a case where the description less 20.
        It should fail the creating process.
        '''

        with pytest.raises(Exception):
            # log in first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            self.type("#description", 'near')
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 100)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")
    
    def test_create_description_over_2000(self, *_):
        '''
        Testing R4-3: The description of the product can
        be arbitrary characters, 
        with a maximum of 2000 characters.
        Method: Input boundary testing
        Analysis: Here is a case where the description over 2000.
        It should fail the creating process.
        '''

        with pytest.raises(Exception):
            # log in first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            self.type("#description", ''.join(["b"] * 2021))
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 100)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")
 
    def test_create_description_longer_title(self, *_):
        '''
        Testing R4-4: Description has to be longer than the product's title.
        Method: Input boundary testing
        Analysis: description is longer than title.
        Expected behaviour: fail to create
        '''

        with pytest.raises(Exception):
            # log in first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", ''.join(["b"] * 50))
            self.type("#description", ''.join(["c"] * 30))
            self.type("#price", 100)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")
    
    def test_create_price_less_10(self, *_):
        '''
        Testing R4-5: Price has to be of range [10, 10000].
        Method: Input boundary testing
        Analysis: test boundary price is less than 10,
        it should fails the creating.
        '''
        with pytest.raises(Exception):
            # login first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            # create listing description
            self.type("#description", "This is a nice place to live near lake")
            self.type("#price", 8)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            self.click("#submit")
            self.click("#btn-submit")
    
    def test_create_price_over_10000(self, *_):
        '''
        Testing R4-5: Price has to be of range [10, 10000].
        Method: Input boundary testing
        Analysis: Here is a case where price_over_10000.
        It should fail the creating process.
        '''
        with pytest.raises(Exception):
            # login first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")
            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            # create listing description
            self.type("#description", "This is a nice place to live near lake")
            self.type("#price", 8)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 20000)
            self.click("#submit")
            self.click("#btn-submit")
    
    def test_date_before_2021_01_02(self, *_):
        '''
        Testing R4-6: last_modified_date must be after 2021-01-02.
        Method: Input boundary testing
        Analysis: test boundary date is before 2021/01/02,
        it should fails the creating.
        '''
        with pytest.raises(Exception):  
            # login first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")

            self.type("#posted_date", date(2018, 1, 9))
            self.type("#title", "good good good")
            # create listing description
            self.type("#description", "This is a nice place to live near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 1000)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")

    def test_date_after_2025_01_02(self, *_):
        '''
        Testing R4-6: last_modified_date must before 2025-01-02.
        Method: Input boundary testing
        Analysis: test boundary date is after 2025/01/02
        it should fails the creating.

        '''
        with pytest.raises(Exception):  
            # login first
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")

            self.type("#posted_date", date(2029, 1, 9))
            self.type("#title", "good good good")
            # create listing description
            self.type("#description", "This is a nice place to live near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 1000)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")

    def test_email_empty(self, *_):
        '''
        Testing R4-7: owner_email cannot be empty. The owner of the 
        corresponding product must exist in the database.
        Method: Input partition
        Analysis: if the password field is empty,
        registration fails and won't go to login page.
        '''
        with pytest.raises(Exception):
            # login first
            self.open(base_url + "/login")
            self.type("#email", "")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")

            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            # create listing description
            self.type("#description", "This is a nice place to live near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 1000)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
    
    def test_repeated_title(self, *_):
        '''
        Testing R4-8: A user cannot create products that have the same title.
        Method: Input partition
        Analysis: if the title is epeated, createing fails.
        '''
        with pytest.raises(Exception):
            # login first
        
            self.open(base_url + "/login")
            self.type("#email", "111@111.com")
            self.type("#password", "123!Abc")
            self.click("#btn-submit")
            self.click("a[href='/create'")

            self.type("#posted_date", date.today())
            self.type("#title", "Good place")
            # create listing description
            self.type("#description", "This is a good place to stay near lake")
            # self.input("#img", "1.png")
            # create listing price
            self.type("#price", 1000)
            # create listing address
            self.type("#address", "333 Horton Street")
            # create listing capacity
            self.type("#capacity", 10)
            # hit the button to save
            self.click("#submit")
            self.click("#btn-submit")

    def test_create_listing(self, *_):
        '''
        Check to see if the database has changed or not
        Extract all the value first, and then
        examine them ony by one
        '''
        path = os.path.abspath(os.getcwd())
        connection = sqlite3.connect(path + "/qbay/data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT title, description, price, address,\
                       capacity FROM Properties WHERE title=?",
                       ("Good place",))
        (title, description, price, address, capacity) = cursor.fetchone()

        connection.close()

        if (title != "Good place"):
            raise Exception("title does not create")

        if (description != "This is a nice place to live near lake"):
            raise Exception("description does not create")

        if (price != 1000):
            raise Exception("price does not create")

        if (address != "333 Horton Street"):
            raise Exception("address does not create")

        if (capacity != 10):
            raise Exception("capacity does not create")
