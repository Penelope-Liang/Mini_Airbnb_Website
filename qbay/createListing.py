'''
This file contains the implementation for listing creation,
following the below requirements.
R4-1: The title of the product has to be alphanumeric-only,
      and space allowed only if it is not as prefix and suffix.
R4-2: The title of the product is no longer than 80 characters.
R4-3: The description of the product can be arbitrary characters,
      with a minimum length of 20 characters and a maximum of 2000 characters.
R4-4: Description has to be longer than the product's title.
R4-5: Price has to be of range [10, 10000].
R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
R4-7: owner_email cannot be empty. The owner of the corresponding
      product must exist in the database.
R4-8: A user cannot create products that have the same title.
'''
from datetime import date
import uuid
import re
import sqlite3


def create_listing_format_checker(listing):
    '''
    This function checks if the listing input satisfies
    all format requirements.
    Parameter: listing - a dictionary
    Return: None
    '''
    # set posted date to today
    # listing["posted_date"] = date.today()

    # R4-1
    if (not re.fullmatch(AccNameReg, listing["title"])):
        raise InvalidListing("No title name")
    # R4-2
    if (len(listing["title"]) > 80):
        raise InvalidListing("title name should less than 80")
    # R4-3
    if not (20 < len(listing["description"]) < 2000):
        raise InvalidListing(
            "description should more than 20, and less than 2000")
    # R4-4
    if not (len(listing["description"]) > len(listing["title"])):
        raise InvalidListing("description have to be longer than title")
    # R4-5
    if (not (int(listing["price"]) > 10 and int(listing["price"]) < 10000)):
        raise InvalidListing("price must between 10 and 10000")
    # R4-6
    if (listing["posted_date"] < date(2021, 1, 2) or
            listing["posted_date"] > date(2025, 1, 2)):
        raise InvalidListing("date must between 1/2/2021 and 1/2/2025")
    # R4-7
    if ("email" not in listing or len(listing["email"]) == 0):
        raise InvalidListing("email can not be empty")


def listing_saving(listing) -> dict:
    '''
    This function saves the new listing data.
    Parameter: listing - a dictionary
    Return: a dictionary
    '''
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT email, user_id FROM Users WHERE email = (?)",
                   (listing["email"],))
    row = cursor.fetchone()

    # check if the owner of the listing exists
    if (row is None):
        raise InvalidListing("This user does not exist")

    (_, user_id) = row
    cursor.execute(
        "SELECT title FROM Properties WHERE title = (?)", (listing["title"],))
    row = cursor.fetchone()
    # R4-8
    # check if the owner has products of the same title
    if (row is not None):
        raise InvalidListing("Title is in use")
    connection.close()

    # set the user_id attribute
    listing["user_id"] = user_id

    # generate a random id for property
    listing["prop_id"] = uuid.uuid4().hex

    # get rid of owner_email pair, since there is no such column
    del listing["email"]

    return listing


def createlisting(listing_save):
    try:
        import os
        print("success")
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        print("connection failed")
        cursor = connection.cursor()
        print("here")

        cursor.execute("INSERT INTO Properties \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (listing_save["prop_id"],
                                                  listing_save["user_id"],
                                                  listing_save["posted_date"],
                                                  listing_save["title"],
                                                  listing_save["description"],
                                                  listing_save.get("img",
                                                                   'pic.png'),
                                                  listing_save["price"],
                                                  listing_save["address"],
                                                  listing_save["capacity"]))
        print("before commit")
        connection.commit()
        print("commit complete")
        connection.close()
    except Exception as e:
        print(e)
        print("Error")


if __name__ == "__main__":
    from regexRepo import AccNameReg
    from exceptions import InvalidListing
    import os
    import sys
    path = os.path.abspath(os.getcwd())
    sys.path.append(path)
    # from models.property import PropertyModel
    # from db import db

    '''
    attention, this function requires some pre-stored data
    in the database, you can run command [in the directory of backend]
    py ./resources/tools/register.py
    '''

    proerpty_1 = {
        "title": "A lighted mansion",

        "description": "This is a mansion sits beside a beach with 16hr+ " +
        "sunshine, beside daily facillities also" +
        "provide with mini swimming pool",
        "price": 5000,
        "email": "JimmyMcgill@SGA.com",
        "posted_date": date.today(),
        "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
        # "postal_code": "L3S4V8",
        "image": "building.png",
        "capacity": 4
    }

    proerpty_2 = {
        "title": "Garbage room",

        "description": "you wnat to live heree??",
        "price": 59,
        "email": "JimmyMcgill@SGA.com",
        "posted_date": date.today(),
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        # "postal_code": "L3S4V8",
        "image": "building.png",
        "capacity": 5

    }
    try:
        create_listing_format_checker(proerpty_1)
        proerpty_1 = listing_saving(proerpty_1)
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Properties \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (proerpty_1["prop_id"],
                        proerpty_1["user_id"],
                        proerpty_1["posted_date"],
                        proerpty_1["title"],
                        proerpty_1["description"],
                        proerpty_1["image"],
                        proerpty_1["price"],
                        proerpty_1["address"],
                        proerpty_1["capacity"]))

        create_listing_format_checker(proerpty_2)
        proerpty_2 = listing_saving(proerpty_2)
        cursor.execute("INSERT INTO Properties \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (proerpty_2["prop_id"],
                        proerpty_2["user_id"],
                        proerpty_2["posted_date"],
                        proerpty_2["title"],
                        proerpty_2["description"],
                        proerpty_2["image"],
                        proerpty_2["price"],
                        proerpty_2["address"],
                        proerpty_2["capacity"]))

        connection.commit()
        connection.close()

    except InvalidListing as IL:
        print(IL.message)


else:
    from .regexRepo import AccNameReg
    from .exceptions import InvalidListing
