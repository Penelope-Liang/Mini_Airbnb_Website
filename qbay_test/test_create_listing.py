import pytest
from datetime import date
from qbay.createListing import create_listing_format_checker
from qbay.exceptions import InvalidListing


def test_create_listing_format_checker_with_valid_format():
    '''
    Testing with a total valid input.
    '''
    listing = {
        "title": "A delighted mansion",
        "description": "This is a mansion sits beside a beach with 16hr" +
        "sunshine, beside daily facillities also provide with mini" +
        "swimming pool",
        "price": 5000,
        "email": "JimmyMcgill@SGA.com",
        "posted_date": date.today()
    }

    try:
        create_listing_format_checker(listing)
    except InvalidListing:
        assert True


def test_create_listing_format_checker_with_bad_title():
    '''
    Testing R4-1, R4-2
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A** delighted mansion ",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_title_char():
    '''
    Testing R4-1: The title of the product has to be alphanumeric-only,
    and space allowed only if it is not as prefix and suffix.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighte???d mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_title_space():
    '''
    Testing R4-1: The title of the product has to be alphanumeric-only,
    and space allowed only if it is not as prefix and suffix.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": " A delighted mansion ",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_title_length():
    '''
    Testing R4-2: The title of the product is no longer than 80 characters.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion A delighted mansion" +
            "A delighted mansion A delighted mansion" +
            "A delighted mansion A delighted mansion" +
            "A delighted mansion A delighted mansion" +
            "A delighted mansion A delighted mansion" +
            "A delighted mansion A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_description_length():
    '''
    Testing R4-3: The description of the product can be arbitrary characters,
    with a minimum length of 20 characters and a maximum of 2000 characters.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A mansion",
            "description": "This is a mansion",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_description_shorter_than_title():
    '''
    Testing R4-4: Description has to be longer than the product's title.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion A delighted mansion",
            "description": "This is a mansion",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_low_price():
    '''
    Testing R4-5: Price has to be of range [10, 10000].
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 1,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_high_price():
    '''
    Testing R4-5: Price has to be of range [10, 10000].
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_old_date():
    '''
    Testing R4-6: last_modified_date must be after 2021-01-02
    and before 2025-01-02.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date(1999, 10, 16)
        }

        create_listing_format_checker(listing)


def test_create_listing_format_checker_with_bad_future_date():
    '''
    Testing R4-6: last_modified_date must be after 2021-01-02
    and before 2025-01-02.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date(2033, 10, 17)
        }

        create_listing_format_checker(listing)


def test_listing_saving_with_no_email():
    '''
    Testing R4-7: owner_email cannot be empty.
    he owner of the corresponding product must exist in the database.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "posted_date": date(2033, 10, 17)
        }

        create_listing_format_checker(listing)


def test_listing_saving_with_same_title():
    '''
    Testing R4-8: A user cannot create products that have the same title.
    '''
    with pytest.raises(InvalidListing):

        listing = {
            "title": "A delighted mansion ",
            "description": "This is a mansion sits beside a beach with 16hr" +
            "sunshine, beside daily facillities also provide with mini" +
            "swimming pool",
            "price": 5000,
            "email": "JimmyMcgill@SGA.com",
            "posted_date": date.today()
        }

        create_listing_format_checker(listing)
