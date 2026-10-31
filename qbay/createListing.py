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
from qbay.db import db
from qbay.models import Users, PropertyModel
from qbay.regexRepo import AccNameReg
from qbay.exceptions import InvalidListing


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
    owner = Users.query.filter_by(email=listing["email"]).first()

    # check if the owner of the listing exists
    if (owner is None):
        raise InvalidListing("This user does not exist")

    user_id = owner.user_id
    # R4-8
    # check if the owner has products of the same title
    if PropertyModel.query.filter_by(title=listing["title"]).first() \
            is not None:
        raise InvalidListing("Title is in use")

    # set the user_id attribute
    listing["user_id"] = user_id

    # generate a random id for property
    listing["prop_id"] = uuid.uuid4().hex

    # get rid of owner_email pair, since there is no such column
    del listing["email"]

    return listing


def createlisting(listing_save):
    try:
        db.session.add(PropertyModel(
            prop_id=listing_save["prop_id"],
            user_id=listing_save["user_id"],
            posted_date=listing_save["posted_date"],
            title=listing_save["title"],
            description=listing_save["description"],
            image=listing_save.get("img", 'pic.png'),
            price=listing_save["price"],
            address=listing_save["address"],
            capacity=listing_save["capacity"]))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        print("Error")
