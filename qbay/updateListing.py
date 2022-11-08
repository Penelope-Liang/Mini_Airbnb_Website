'''
R5-1: One can update all attributes of the listing,
except owner_id and last_modified_date.
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated when the update
operation is successful.
R5-4: When updating an attribute, one has to make sure that
it follows the same requirements as above.
'''
from datetime import date
import re
import sqlite3


def update_listing_format_checker_1(proerpty_1):
    '''
    Check update_lising prop_id format
    '''
    if "user_id" in proerpty_1 or "posted_date" in proerpty_1:
        raise InvalidUpdateListing(
            "user_id or posted date should not be in side the ")


def updating_data(proerpty_1) -> dict:
    '''
    Update property data
    '''
    import pathlib
    path = pathlib.Path(__file__).parent.joinpath("data.db")
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Properties WHERE prop_id = (?)",
        (proerpty_1["prop_id"],))

    row = cursor.fetchone()
    connection.close()

    print(row)

    old_property = {
        "title": row[3],
        "description": row[4],
        "image": row[5],
        "price": row[6],
        "address": row[7],
        "capacity": row[8],
    }

    print(old_property)

    print(proerpty_1)

    if (proerpty_1["price"] != ''

        and
            old_property["price"] > proerpty_1["price"]):
        raise InvalidUpdateListing("Price can only go up")

    for key in proerpty_1:
        if key != "prop_id" and proerpty_1[key] == '':
            proerpty_1[key] = old_property[key]

    print("the new prop is ", proerpty_1)

    # check the property_1
    update_listing_format_checker_2(proerpty_1)

    proerpty_1["posted_date"] = date.today()

    return proerpty_1


def update_listing_format_checker_2(proerpty_1):
    '''
    Check the format of update items including
    title, description, price
    Check email is not empty
    '''
    if (not re.fullmatch(AccNameReg, proerpty_1["title"])):
        raise InvalidUpdateListing("No title name")

    if (len(proerpty_1["title"]) > 80):
        raise InvalidUpdateListing("title name should less than 80")

    if (not (len(proerpty_1["description"]) > 20
             and len(proerpty_1["description"]) < 2000)):
        raise InvalidUpdateListing(
            "description should more than 20, and less than 2000")

    if (not (len(proerpty_1["description"]) > len(proerpty_1["title"]))):
        raise InvalidUpdateListing("description have to be longer than title")

    if (not (proerpty_1["price"] > 10 and proerpty_1["price"] < 10000)):
        raise InvalidUpdateListing("price must between 10 and 10000")

    if ("email" not in proerpty_1 or len(proerpty_1["email"]) == 0):
        raise InvalidUpdateListing("email can not be empty")


def updateInfo(listing_save):
    try:
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        print("this is the path  ", path)
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()

        print("data: {}".format(listing_save))

        update_sql = 'update Properties set posted_date=?,' \
                     'title=?,description=?,' \
                     'image=?, price=?,address=?,capacity=? where prop_id=?'

        cursor.execute(update_sql, (
            listing_save["posted_date"],
            listing_save["title"],
            listing_save["description"],
            listing_save["image"],
            listing_save["price"],
            listing_save["address"],
            listing_save["capacity"],
            listing_save["prop_id"]
        ))

        connection.commit()
        connection.close()
    except Exception:
        print("Error")


if __name__ == "__main__":
    from regexRepo import AccNameReg
    from exceptions import InvalidUpdateListing
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

    # we don't have last_modify date, but I think you can use posted_date
    proerpty_1 = {
        "title": "A lighted mansion",
        "prop_id": "c56340108a134fe9a4882c9190cc5229",
        "description": "This is a mansion sits beside a beach with 16hr+ " +
        "sunshine, beside daily facillities also" +
        "provide with mini swimming pool",
        "price": 9999,
        "email": "JimmyMcgill@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
        "image": "building.png",
        "capacity": 4
    }

    proerpty_2 = {
        "title": "Garbage room 2",
        "prop_id": "c56340108a134fe9a4882c9190cc5229",
        "description": "you wnat to live heree??",
        "price": 5900,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }

    update_listing_format_checker_1(proerpty_1)
    updating_data(proerpty_1)

    update_listing_format_checker_1(proerpty_2)
    updating_data(proerpty_2)


else:
    from .regexRepo import AccNameReg
    from .exceptions import InvalidUpdateListing
    import os
