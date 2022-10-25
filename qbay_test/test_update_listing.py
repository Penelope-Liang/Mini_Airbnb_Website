import pytest
from qbay.exceptions import InvalidUpdateListing
# from datetime import date
from qbay.updateListing\
    import update_listing_format_checker_1, updating_data
# from resources.tools.exceptions import InvalidUpdateListing


def test_updatelisting_update_title():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Treehouse hosted by Christopher",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "you want to live heree??",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_update_description():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "Good plavce to live",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_update_price():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "you want to live heree??",
            "price": 9801,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_not_update_title():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_not_update_description():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_not_update_address():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "Wonderful place",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)


def test_updatelisting_not_update_price():
    with pytest.raises(InvalidUpdateListing):
        update = {
            "title": "Garbage room",
            "user_id": "20a7066e8e844759a99a20ecbd6935fe",
            "description": "Wonderful place",
            "price": 59,
            "email": "Garbage@SGA.com",
            "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
            "image": "building.png",
            "capacity": 5

        }
        update_listing_format_checker_1(update)
        updating_data(update)
