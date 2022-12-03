import os
import pytest
import time
from datetime import datetime
import threading
from werkzeug.serving import make_server
import sqlite3
import pathlib
from qbay import app
path = pathlib.Path().resolve()
path = path.joinpath("qbay").joinpath("data.db")
'''
This file defines what to do BEFORE running any test cases:

'''
test_data = [
    {
        "tsc_id": "1d0027b7bd3e4587861dd32a16f213c7",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "property_id": "dfa708de23b541808202133f2dde7c58",
        "tsc_date": datetime.now(),
        "tsc_price": "2000.0",
        "check_in_date": "2022-07-22T00:00",
        "check_out_date": "2022-07-23T00:00",
        "guest_number": 1
    },

    {
        "tsc_id": "3654c0292f134c0c800b9d",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "property_id": "5f6d0cf33adf486abe680063816d4f39",
        "tsc_date": datetime.now(),
        "tsc_price": "1500.0",
        "check_in_date": "2022-08-22T00:00",
        "check_out_date": "2022-08-23T00:00",
        "guest_number": 1
    },

    {
        "tsc_id": "0e08f32bd4cd4b5d81b4ea693f2c286e",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "property_id": "cf828f35ad7243108a843770ad34f192",
        "tsc_date": datetime.now(),
        "tsc_price": "1000.0",
        "check_in_date": "2022-09-06T00:00",
        "check_out_date": "2022-09-07T00:00",
        "guest_number": 1
    },

    {
        "tsc_id": "3654f32bd4cd4b5d81b4eac414e2f32a",
        "user_id": "b36524c626e64b15b3dcebb6d21dd5d8",
        "property_id": "ebbc91cdf0f646e9993222418c39c69d",
        "tsc_date": datetime.now(),
        "tsc_price": "35.0",
        "check_in_date": "2022-02-01T08:30",
        "check_out_date": "2022-02-28T08:30",
        "guest_number": 3,
    }
]


def pytest_sessionstart():
    '''
    Delete database file if existed. So testing can start fresh.
    '''
    print('Setting up environment..')
    db_file = 'db.sqlite'
    if os.path.exists(db_file):
        os.remove(db_file)

    # injecting data

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    for data in test_data:
        cursor.execute("INSERT INTO Transactions \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (data["tsc_id"], data["user_id"],
                        data["property_id"], data["tsc_date"],
                        data["tsc_price"], data["check_in_date"],
                        data["check_out_date"], data["guest_number"]))
        connection.commit()

    connection.close()


def pytest_sessionfinish():
    '''
    Optional function called when testing is done.
    Do nothing for now
    '''
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    for data in test_data:
        cursor.execute("DELETE FROM Transactions \
            WHERE tsc_id = (?)",
                       (data["tsc_id"], ))
        connection.commit()

    connection.close()


base_url = 'http://127.0.0.1:{}'.format(8080)


class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # import necessary routes

        from qbay import controllers
        self.srv = make_server('127.0.0.1', 8080, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('running')
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


@pytest.fixture(scope="session", autouse=True)
def server():
    # create a live server for testing
    # with a temporary file as database
    server = ServerThread()
    server.start()
    time.sleep(5)
    yield
    server.shutdown()
    time.sleep(2)
