import pytest
import pathlib
from qbay.createListing import create_listing_format_checker, \
    listing_saving, createlisting
import os
import sqlite3
from datetime import date
import random

'''
The file test the sql injection against 
the create listing file.
The following program read in the injection code, and input the 
them each line for every input, it only inject when they have 
correct format.
'''

# Read all injection line by line to the list
path = pathlib.Path(__file__)\
    .resolve().parent\
    .joinpath("Generic_SQLI.txt")
with open(path) as file:
    lines = [line.rstrip() for line in file]


def test_test_createlisting():

    for line in lines:
        random_int = random.randint(1, 1000)
        random_int2 = random.randint(1, 1000)
        random_string = str(random_int) + str(random_int2)

        injection_template = {
            "email": "111@111.com",
            "posted_date": date.today(),
            "title": "Farm stay" + random_string,
            "description": "Relax with the whole family at this peaceful \
                            5 Bedroom Villa overlooking Hout Bay Beach",
            "price": 1500,
            "address": "333 Division Street",
            "capacity": 4
        }
    
        for key in injection_template:
            with pytest.raises(Exception):
                listing = {**injection_template}
                listing[key] = line
                if key == 'description' and len(line) > 20:
                    print(1)

                # check listing format and save
                create_listing_format_checker(listing)
                reg_listing = listing_saving(listing)
                # create listing to the database
                createlisting(reg_listing)

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

                if row is not None:
                    cursor.execute("DELETE FROM \
                                   Properties WHERE posted_date=? \
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
                    connection.close()
                    raise Exception("injection didn't exist")

                # If injection exists, it will be false
                connection.close()