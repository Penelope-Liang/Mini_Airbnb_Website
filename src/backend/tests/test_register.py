import pytest
from resources import register_format_checker, register_saving
from resources import InvaildRegister


def test_register_format_checker_with_valid_format():

    user = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "password": "Best_lawer123",
        "email": "JimmyMcgill@SGA.com",
        "profile_photo": "Jimmy_McGill_BCS_S3.png",
        "about": "Hi, I am saul"
    }

    try:
        register_format_checker(user)
    except InvaildRegister as IR:
        assert False, IR.case


def test_register_format_checker_with_bad_acc_name():

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

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

    with pytest.raises(InvaildRegister):

        user = {
            "acc_name": "Saul Goodman",
            "first_name": "Jimmy",
            "last_name": "Mcgill",
            "password": "Best_lawer123",
            "email": "JimmyMcgill@SGA.com",
            "profile_photo": "Jimmy_McGill_BCS_S3.png",
            "about": "Hi, I am saul",
            "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
            "postal_code": "L3S4V8"
        }

        register_saving(user)


def test_register_saving_should_return_user_id():

    user2 = {
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM2.com",
        "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!",
    }

    new_user = register_saving(user2)
    assert new_user["user_id"] is not None


def test_register_saving_should_return_balance_equals_100():

    user2 = {
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM2.com",
        "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!",
    }

    new_user = register_saving(user2)
    assert new_user["balance"] == 100


def test_register_saving_should_return_no_address():

    user2 = {
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM2.com",
        "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!",
    }

    new_user = register_saving(user2)
    assert new_user["address"] is None


def test_register_saving_should_return_no_postal_code():

    user2 = {
        "acc_name": "Giselle",
        "first_name": "Kim",
        "last_name": "Wexler",
        "password": "Kim$$123321",
        "email": "KimKim@HHM2.com",
        "profile_photo": "Kim_Wexler_BCS_S5.png",
        "about": "Hello, I am Kim!",
    }

    new_user = register_saving(user2)
    assert new_user["postal_code"] is None
