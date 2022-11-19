import pytest
import pathlib
from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from qbay.createListing import create_listing_format_checker
from unittest.mock import patch
import os
import sqlite3
from datetime import date

path = pathlib.Path(__file__).resolve().parent.joinpath("Generic_SQLI.txt")
with open(path) as file:
    lines = [line.rstrip() for line in file]


class Security_Of_SQL_Injection_Tes(BaseCase):
    def test_test_createlisting(self, *_):
        for line in lines:
            correct_createlisting = {
                "#posted_date": date.today(),
                "#title": "Nice Town House",
                "#description": "Relax with the whole family at this peaceful \
                                5 Bedroom Villa overlooking Hout Bay Beach",
                "#price": 1500,
                "#address": "444 Division Street",
                "#capacity": 4
            }
    
            for key1 in correct_createlisting:
                self.open(base_url + "/login")
                self.type("#email", "111@111.com")
                self.type("#password", "123!Abc")
                self.click("#btn-submit")
                self.click("a[href='/create'")
                self.type(key1, line)

                for key2, value in correct_createlisting.items():
                    if key2 != key1:
                        self.type(key2, value)

                try:
                    self.click("#submit")
                    listing = {
                        "email": "111@111.com",
                        "posted_date": correct_createlisting["#posted_date"],
                        "title": correct_createlisting["#title"],
                        "description": correct_createlisting["#description"],
                        "price": correct_createlisting["#price"],
                        "address": correct_createlisting["#address"],
                        "capacity": correct_createlisting["#capacity"]
                    }

                    if key1 == "posted_date":
                        listing["posted_date"] = line
                    elif key1 == "title":
                        listing["title"] = line
                    elif key1 == "description":
                        listing["description"] = line
                    elif key1 == "price":
                        listing["price"] = line
                    elif key1 == "address":
                        listing["address"] = line
                    elif key1 == "capacity":
                        listing["capacity"] = line
                    
                    create_listing_format_checker(listing)

                    path = os.path.abspath(os.getcwd())
                    connection = sqlite3.connect(path + "/qbay/data.db")
                    cursor = connection.cursor()
                    cursor.execute("SELECT * \
                                FROM Properties WHERE posted_date=? \
                                and title=?\
                                and description=? \
                                and price = ? \
                                and address = ?\
                                and capacity = ?", 
                                (listing["posted_date"],
                                    listing["title"],
                                    listing["description"],
                                    listing["price"],
                                    listing["address"],
                                    listing["capacity"]))
                    row = cursor.fetchone()
                    connection.close()

                    if row is None:
                        raise Exception("Injection exists")
                    assert True

                except Exception:
                    assert False
