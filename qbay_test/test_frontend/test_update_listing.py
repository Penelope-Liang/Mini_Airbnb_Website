from seleniumbase import BaseCase
import os
import sqlite3
from qbay_test.conftest import base_url
import pytest

import random

'''
This file tests the function of updating the listing
using random int as string to make sure each
time testing using different value
'''
random_int = random.randint(1, 1000)
random_string = str(random_int)
changed_name = "Los Pollos Hermanos " + random_string
changed_descri = "welcome to Los Pollos Hermanos, I am Gus Fring, \
                  we don't welcome Salamanca " + random_string
changed_address = random_string + " Burleigh St, Apsley, ON K0L 1A0"

path = os.path.abspath(os.getcwd())
connection = sqlite3.connect(path + "/qbay/data.db")
cursor = connection.cursor()
cursor.execute("SELECT price FROM Properties WHERE prop_id=?",
               ("5f1f29182d7e47b094e9f932ef19a976",))
(changed_price,) = cursor.fetchone()
connection.close()


class FrontEndHomePageTest(BaseCase):

    def test_update_title_and_desciption(self, *_):
        '''
        This is a valid change, all input satisfy the 
        requirements
        '''

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

        # start editing and the name and description
        self.type("#title", changed_name)
        self.type("#description", changed_descri)
        self.click("#submit")

        self.click("#btn-submit")

    def test_update_price_capacity_address(self, *_):
        '''
        This is a valid change, all input satisfy the 
        requirements
        '''

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

        self.type("#price", changed_price + 0.5)
        self.type("#capacity", str(random_int % 5))
        self.type("#address", changed_address)
        self.click("#submit")

        self.click("#btn-submit")

    '''
    Exhaustive Input Testing:
        - test_update_with_wrong_title
        - test_update_with_wrong_title2
    Try all of the possible input of title:
    
    '''

    def test_update_with_wrong_title(self, *_):
        '''
        R4-1: The title of the product has to be alphanumeric-only,
        and space allowed only if it is not as prefix and suffix.
        '''

        with pytest.raises(Exception):
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

            self.type("#title", "xxxx^^^^")
            self.click("#submit")
            self.click("#btn-submit")

    def test_update_with_wrong_title2(self, *_):
        '''
        R4-2: The title of the product is no longer than 80 characters.
        '''

        with pytest.raises(Exception):
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

            self.type("#title", ''.join(["a"] * 100))
            self.click("#submit")
            self.click("#btn-submit")

    '''
    Output Partition Testing:
        - test_update_with_wrong_description
        - test_update_with_wrong_description2
        - test_update_with_wrong_description3
    design different input length of description casue differnet output
    '''

    def test_update_with_wrong_description(self, *_):
        '''
        R4-3: The description of the product 
        can be arbitrary characters,
        with a minimum length of 20 characters 
        and a maximum of 2000 characters.
        '''

        with pytest.raises(Exception):
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

            self.type("#description", 'a')
            self.click("#submit")
            self.click("#btn-submit")

    def test_update_with_wrong_description2(self, *_):
        '''
        R4-3: The description of the product can 
        be arbitrary characters,
        with a minimum length of 20 characters 
        and a maximum of 2000 characters.
        '''

        with pytest.raises(Exception):
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

            self.type("#description", ''.join(["a"] * 4000))
            self.click("#submit")
            self.click("#btn-submit")

    def test_update_with_wrong_description3(self, *_):
        '''
        R4-4: Description has to be longer than the product's title.
        '''

        with pytest.raises(Exception):
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

            self.type("#title", ''.join(["a"] * 500))
            self.type("#description", ''.join(["a"] * 200))
            self.click("#submit")
            self.click("#btn-submit")

    def test_update_with_wrong_price_value(self, *_):
        '''
        R5-2: Price can be only increased but cannot be decreased :)
        '''
        with pytest.raises(Exception):
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

            self.type("#price", changed_price - 0.5)
            self.click("#submit")
            self.click("#btn-submit")

    '''
    Input Boundary Testing:
        test_update_with_wrong_price_value2
        test_update_with_wrong_price_value3
    try the lower boundry and the upper boundry of the price
    '''

    def test_update_with_wrong_price_value2(self, *_):
        '''
        R4-5: Price has to be of range [10, 10000].
        '''

        with pytest.raises(Exception):
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

            self.type("#price", 9)
            self.click("#submit")
            self.click("#btn-submit")

    def test_update_with_wrong_price_value3(self, *_):
        '''
        R4-5: Price has to be of range [10, 10000].
        '''

        with pytest.raises(Exception):
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

            self.type("#price", 10001)
            self.click("#submit")
            self.click("#btn-submit")


def test_are_they_changed():
    '''
    Check to see if the database has changed or not
    Extract all the value first, and then
    examine them ony by one
    '''
    path = os.path.abspath(os.getcwd())
    connection = sqlite3.connect(path + "/qbay/data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, \
                   price, address, capacity \
                   FROM Properties WHERE prop_id=?",
                   ("5f1f29182d7e47b094e9f932ef19a976",))
    (title, description,
     price, address, capacity) = cursor.fetchone()

    connection.close()

    if (title != changed_name):
        raise Exception("title is not updated")

    if (description != changed_descri):
        raise Exception("description is not updated")

    if (price != changed_price + 0.5):
        raise Exception("price is not updated")

    if (address != changed_address):
        raise Exception("address is not updated")

    if (capacity != random_int % 5):
        raise Exception("capacity is not updated")
