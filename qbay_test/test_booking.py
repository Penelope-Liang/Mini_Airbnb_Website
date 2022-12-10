from qbay.exceptions import InvalidBooking
import pytest
from qbay.booking import booking_requirement_checking, save_transaction_record


def test_user_book_his_own_listing():
    '''
      A user cannot book a listing for his/her listing.
    '''
    test_tsc = {
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
        "check_in_date": "2022-06-01T08:30",
        "check_out_date": "2022-06-04T08:30",
        "guest_number": 2,
    }

    with pytest.raises(InvalidBooking):
        booking_requirement_checking(test_tsc)


def test_costs_more_than_balance():
    '''
      A user cannot book a listing that costs 
        more than his/her balance.
    '''
    test_tsc = {
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",

        # check this
        "check_in_date": "1022-04-02T08:30",

        # this user aint gonna leave, yo
        # 5022 I must be a grand*100 pa
        "check_out_date": "5022-10-30T08:30",
        "guest_number": 3,
    }

    with pytest.raises(InvalidBooking):
        booking_requirement_checking(test_tsc)


def test_overlapped_dates():
    '''
      A user cannot book a listing that is
        already booked with the overlapped dates.

      check_in_date       check_out_date
             C1----------------------C2

                user_check_in_date         user_check_out_date
                    U1--------------------------------U2
    '''
    test_tsc = {
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
        "check_in_date": "2022-02-05T08:30",
        "check_out_date": "2022-04-15T08:30",
        "guest_number": 3,
    }

    with pytest.raises(InvalidBooking):
        booking_requirement_checking(test_tsc)


def test_overlapped_dates2():
    '''
      A user cannot book a listing that is
        already booked with the overlapped dates.

        check_in_date       check_out_date
                     C1----------------------C2

        user_check_in_date         user_check_out_date
            U1----------------------------U2
    '''
    test_tsc = {
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
        "check_in_date": "2022-01-01T08:30",
        "check_out_date": "2022-02-21T08:30",
        "guest_number": 3,
    }

    with pytest.raises(InvalidBooking):
        booking_requirement_checking(test_tsc)


def test_overlapped_dates3():
    '''
      A user cannot book a listing that is
        already booked with the overlapped dates.

        check_in_date                   check_out_date
         C1-----------------------------------C2

            user_check_in_date       user_check_out_date
                U1----------------------U2
    '''
    test_tsc = {
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
        "check_in_date": "2022-01-01T08:30",
        "check_out_date": "2022-07-20T08:30",
        "guest_number": 3,
    }

    with pytest.raises(InvalidBooking):
        booking_requirement_checking(test_tsc)


def test_user_balance_changed():
    '''
      check if the user balance changed after 
        booking
    '''
    test_tsc = {
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
        "check_in_date": "2022-09-01T08:30",
        "check_out_date": "2022-09-10T08:30",
        "guest_number": 3,
    }

    import sqlite3
    import pathlib

    path = pathlib.Path().resolve()
    path = path.joinpath("qbay").joinpath("data.db")
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT balance FROM Users WHERE user_id = (?)",
        (test_tsc["user_id"], ))
    (prevBalance, ) = cursor.fetchone()

    # check the inputs
    rst = booking_requirement_checking(test_tsc)

    # save to data base
    save_transaction_record(rst)

    cursor.execute(
        "SELECT balance FROM Users WHERE user_id = (?)",
        (test_tsc["user_id"], ))
    (curBalance, ) = cursor.fetchone()

    cursor.execute("DELETE FROM \
                    Transactions WHERE tsc_id=(?)",
                   (rst["tsc_id"],))

    if float(curBalance) == float(prevBalance):

        connection.close()
        raise Exception("Balance did not change")

    cursor.execute("UPDATE Users SET \
                    balance = (?) WHERE user_id = (?)",
                   (5000, test_tsc["user_id"]))
    connection.commit()
    connection.close()
