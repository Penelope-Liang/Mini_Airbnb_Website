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
from qbay.db import db
from qbay.models import PropertyModel
from qbay.regexRepo import AccNameReg
from qbay.exceptions import InvalidUpdateListing


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
    row = PropertyModel.query.with_entities(
        PropertyModel.title, PropertyModel.description, PropertyModel.image,
        PropertyModel.price, PropertyModel.address, PropertyModel.capacity
    ).filter_by(prop_id=proerpty_1["prop_id"]).first()

    old_property = {
        "title": row[0],
        "description": row[1],
        "image": row[2],
        "price": row[3],
        "address": row[4],
        "capacity": row[5],
    }

    if (proerpty_1["price"] != ''

        and
            float(old_property["price"]) > float(proerpty_1["price"])):
        raise InvalidUpdateListing("Price can only go up")

    for key in proerpty_1:
        if key != "prop_id" and proerpty_1[key] == '':
            proerpty_1[key] = old_property[key]

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

    if (not (float(proerpty_1["price"]) > 10
             and float(proerpty_1["price"]) < 10000)):
        raise InvalidUpdateListing("price must between 10 and 10000")

    if ("email" not in proerpty_1 or len(proerpty_1["email"]) == 0):
        raise InvalidUpdateListing("email can not be empty")


def updateInfo(listing_save):
    try:
        PropertyModel.query.filter_by(prop_id=listing_save["prop_id"]).update({
            "posted_date": listing_save["posted_date"],
            "title": listing_save["title"],
            "description": listing_save["description"],
            "image": listing_save["image"],
            "price": listing_save["price"],
            "address": listing_save["address"],
            "capacity": listing_save["capacity"],
        })
        db.session.commit()
    except Exception:
        db.session.rollback()
        print("Error")
