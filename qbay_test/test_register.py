import pytest
from qbay.register import register_format_checker, register_saving
# from qbay.exceptions import *


def test_register_format_checker_with_valid_format():
    '''
    No requirement, normal ID
    '''
    user = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "password": "Best_lawer123!",
        "email": "JimmyMcgill@SGA.com",
        "profile_photo": "Jimmy_McGill_BCS_S3.png",
        "about": "Hi, I am saul"
    }

    try:
        register_format_checker(user)
    except Exception as IR:
        assert False, IR.case


def test_register_format_checker_with_bad_acc_name():
    '''
    R1-5: User name has to be non-empty, alphanumeric-only, and space
        allowed only if it is not as the prefix or suffix.
    '''
    with pytest.raises(Exception):

        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }
        register_format_checker(user)


def test_register_format_checker_with_bad_password_plain_numbers():
    '''
    R1-4: Password has to meet the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character.
    '''
    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "123456789",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_password_plain_characters():
    '''
    R1-4: Password has to meet the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character.
    '''
    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "qwerty",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_password_no_special_ctrs():
    '''
    R1-4: Password has to meet the required complexity: minimum length 6,
            at least one upper case, at least one lower case,
            and at least one special character.
    '''
    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Qwerty123",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_password_no_uppercase():
    '''
    R1-4: Password has to meet the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_password_all_uppercase():

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "QWERTY123!",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_password_all_lowercase():
    '''
    R1-4: Password has to meet the required complexity: minimum length 6,
        at least one upper case, at least one lower case,
        and at least one special character.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_email_no_At_sign():
    '''
    R1-3: The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for
        a human-friendly explanation).
        You can use external libraries/imports.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgillSGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_email_no_dot_com():
    '''
    R1-3: The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for
        a human-friendly explanation).
        You can use external libraries/imports.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@SGA",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_email_no_prefix():
    '''
    R1-3: The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for
        a human-friendly explanation).
        You can use external libraries/imports.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_bad_email_no_suffix():
    '''
    R1-3: The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for
        a human-friendly explanation).
        You can use external libraries/imports.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_address():
    '''
    R1-8: Shipping address is empty at the time of registration.
    '''
    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul",
            "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico"
        }

        register_format_checker(user)


def test_register_format_checker_with_postal_code():
    '''
    R1-9: Postal code is empty at the time of registration.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul",
            "postal_code": "L3S4V8"
        }

        register_format_checker(user)


def test_register_format_checker_with_postal_code_and_address():
    '''
    R1-8: Shipping address is empty at the time of registration.
    R1-9: Postal code is empty at the time of registration.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul",
            "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
            "postal_code": "L3S4V8"
        }

        register_format_checker(user)


def test_register_format_checker_with_no_email():
    '''
    R1-1: Email cannot be empty. password cannot be empty.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_no_password():
    '''
    R1-1: Email cannot be empty. password cannot be empty.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_empty_email():
    '''
    R1-1: Email cannot be empty. password cannot be empty.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_format_checker_with_empty_password():
    '''
    R1-1: Email cannot be empty. password cannot be empty.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul"
        }

        register_format_checker(user)


def test_register_saving_with_used_email():
    '''
    R1-7: If the email has been used, the operation failed.
    '''

    with pytest.raises(Exception):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "DimDim@HHM.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul",
            "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
            "postal_code": "L3S4V8"
        }

        register_saving(user)
