import pytest
from qbay.updateUserProfile import update_user_checker
from qbay.exceptions import InvalidUserUpdate


def test_user_update_format_checker_with_bad_acc_name():
    '''
    R3-2
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "  !",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@SGA.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2"
        }

        update_user_checker(user)


def test_user_update_format_checker_with_bad_email_no_At_sign():
    '''
    R3-4
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgillSGA.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2"
        }

        update_user_checker(user)


def test_user_update_format_checker_with_bad_email_no_dot_com():
    '''
    R3-4
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@SGA",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2"
        }

        update_user_checker(user)


def test_user_update_format_checker_with_bad_email_no_prefix():
    '''
    R3-4
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "@SGA.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2"
        }

        update_user_checker(user)


def test_user_update_format_checker_with_bad_email_no_suffix():
    '''
    R3-4
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2"
        }

        update_user_checker(user)


def test_user_update_format_checker_with_special_characters():
    '''
    R3-2
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "T5J2Z2!"
        }

        update_user_checker(user)


def test_user_update_format_checker_is_all_number_Canada_postal_code():
    '''
    R3-3
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "111111"
        }

        update_user_checker(user)


def test_user_update_format_checker_is_all_letters_Canada_postal_code():
    '''
    R3-3
    '''
    with pytest.raises(InvalidUserUpdate):
        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "email": "JimmyMcgill@.com",
            "address": "2470 137th Avenue, Edmonton",
            "postal_code": "aaaaaa"
        }

        update_user_checker(user)
