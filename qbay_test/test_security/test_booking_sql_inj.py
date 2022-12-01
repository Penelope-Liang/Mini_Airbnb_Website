import pytest
import pathlib
from qbay.booking import booking_requirement_checking, save_transaction_record
import os
import sqlite3
import datetime
import random
import time

'''
The file test the sql injection against 
the booking file.
The following program read in the injection code, and input the 
them each line for every input, it only inject when they have 
correct format.
'''

# Read all injection line by line to the list
path = pathlib.Path(__file__)\
    .resolve().parent\
    .joinpath("Generic_SQLI.txt")
with open(path) as file:
    lines = [line.rstrip() for line in file]

a1=(2021,1,1,0,0,0,0,0,0)
a2=(2025,12,31,23,59,59,0,0,0)
start = time.mktime(a1)
end = time.mktime(a2)

def test_test_booking():
        
    for line in lines:
        t1 = random.randint(start, end)
        date_to = time.localtime(t1)
        start_date=datetime.datetime.strptime(time.strftime("%Y-%m-%dT%H:%M", date_to), "%Y-%m-%dT%H:%M")
        end_date = start_date + datetime.timedelta(days=30)


        injection_template = {
            "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
            "prop_id": "ebbc91cdf0f646e9993222418c39c69d",
            "check_in_date": start_date.strftime("%Y-%m-%dT%H:%M"),
            "check_out_date": end_date.strftime("%Y-%m-%dT%H:%M"),
            "guest_number": 6,
        }

        for key in injection_template:

            '''
            We select a key to be changed to injection
            code
            '''

            with pytest.raises(Exception):

                booking = {**injection_template}
                booking[key] = line
                reg_booking = booking_requirement_checking(booking)
                save_transaction_record(reg_booking)

                path = os.path.\
                    abspath(os.getcwd())
                connection = sqlite3.connect(
                    path + "/qbay/data.db")
                cursor = connection.cursor()

                cursor.execute("SELECT * \
                                FROM Transactions WHERE user_id = ?\
                                and prop_id = ? \
                                and check_in_date=? \
                                and check_out_date=?\
                                and guest_number = ?",
                                (reg_booking["user_id"],
                                reg_booking["prop_id"],
                                reg_booking["check_in_date"],
                                reg_booking["check_out_date"],
                                reg_booking["guest_number"]))

                row = cursor.fetchone()

                if row is not None:
                    cursor.execute("DELETE \
                                FROM Transactions WHERE user_id = ?\
                                and prop_id = ? \
                                and check_in_date=? \
                                and check_out_date=?\
                                and guest_number = ?",
                                (reg_booking["user_id"],
                                reg_booking["prop_id"],
                                reg_booking["check_in_date"],
                                reg_booking["check_out_date"],
                                reg_booking["guest_number"]))
                    connection.commit();
                    connection.close()
                    raise Exception("injection didn't exist")

                # If injection exists, it will be false
                # As no Expcetion is raise
                connection.commit();
                connection.close()
