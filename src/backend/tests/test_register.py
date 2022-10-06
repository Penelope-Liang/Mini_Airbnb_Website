from resources import register_format_checker, register_saving
from resources import InvaildRegister


def test_register_format_checker_with_valid_format():
    print("testing")

    user = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "password": "Best_lawer123",
        "email": "JimmyMcgill@SGA.com",
        "profile_photo": "https://en.wikipedia.org/wiki/Saul_Goodman#/media/File:Jimmy_McGill_BCS_S3.png",
        "about": "Hi. I'm Saul Goodman. Did you know that you have rights?"
    }

    try:
        register_format_checker(user)
    except InvaildRegister as IR:
        assert False, "The account saul goodman should be valid, something wrong: " + IR.case
