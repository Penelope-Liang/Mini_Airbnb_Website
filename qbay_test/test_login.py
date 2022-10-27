import pytest
from qbay.login import login_checker
from qbay.exceptions import InvalidLogin


def test_login_format_checker_with_valid_format():
    '''
    Normal case, no requirement
    '''

    user = {
        "password": "Best_lawyer123",
        "email": "JimmyMcgill@SGA.com"
    }

    try:
        login_checker(user)
    except InvalidLogin as IR:
        assert True, IR.case


def test_login_format_checker_with_bad_password_plain_numbers():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "123456789",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_plain_characters():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_no_special_ctrs():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Qwerty123",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_no_uppercase():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_all_uppercase():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "QWERTY123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_all_lowercase():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_At_sign():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgillSGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_dot_com():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgill@SGA"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_prefix():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_suffix():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgill@.com"
        }

        login_checker(user)


def test_login_format_checker_with_empty_email():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": ""
        }

        login_checker(user)


def test_login_format_checker_with_empty_password():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''

    with pytest.raises(InvalidLogin):

        user = {
            "password": "",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)
