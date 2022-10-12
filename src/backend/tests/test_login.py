
import pytest
from resources.tools.login import login_checker
from resources.tools.exceptions import InvalidLogin


def test_login_format_checker_with_valid_format():

    user = {
        "password": "Best_lawyer123",
        "email": "JimmyMcgill@SGA.com"
    }

    try:
        login_checker(user)
    except InvalidLogin as IR:
        assert True, IR.case


def test_login_format_checker_with_bad_password_plain_numbers():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "123456789",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_plain_characters():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_no_special_ctrs():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Qwerty123",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_no_uppercase():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_all_uppercase():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "QWERTY123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_password_all_lowercase():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "qwerty123!",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_At_sign():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgillSGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_dot_com():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgill@SGA"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_prefix():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "@SGA.com"
        }

        login_checker(user)


def test_login_format_checker_with_bad_email_no_suffix():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": "JimmyMcgill@.com"
        }

        login_checker(user)


def test_login_format_checker_with_empty_email():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "Best_lawyer123",
            "email": ""
        }

        login_checker(user)


def test_login_format_checker_with_empty_password():

    with pytest.raises(InvalidLogin):

        user = {
            "password": "",
            "email": "JimmyMcgill@SGA.com"
        }

        login_checker(user)
