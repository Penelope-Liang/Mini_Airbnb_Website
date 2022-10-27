import pytest
from qbay.exceptions import InvalidUpdateListing
# from datetime import date
from qbay.updateListing\
    import update_listing_format_checker_1, updating_data
# from resources.tools.exceptions import InvalidUpdateListing


def test_updatelisting_update_title():
    '''
    R5-1: One can update all attributes of the listing,
    except owner_id and last_modified_date.
    '''
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
    '''
    R5-1: One can update all attributes of the listing,
    except owner_id and last_modified_date.
    '''
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
    '''
    R5-1: One can update all attributes of the listing,
    except owner_id and last_modified_date.
    '''
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
    '''
    R5-1: One can update all attributes of the listing,
    except owner_id and last_modified_date.
    '''
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
    '''
    R5-1: One can update all attributes of the listing,
    except owner_id and last_modified_date.
    '''
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
    '''
    R5-4: When updating an attribute, one has to make sure that
    it follows the same requirements as above.
    '''
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
    '''
    R5-3: last_modified_date should be updated when the update
    operation is successful.
    '''
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
