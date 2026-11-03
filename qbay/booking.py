'''
A user cannot book a listing for his/her listing.
A user cannot book a listing that costs
    more than his/her balance.
A user cannot book a listing that is
    already booked with the overlapped dates.
A booked listing will show up on the
    user's home page (up-coming stages).
'''

import uuid
from datetime import datetime
from qbay.db import db
from qbay.exceptions import InvalidBooking
from qbay.models import Users, PropertyModel, TscModel


def booking_requirement_checking(tsc) -> dict:
    '''
    This function checks if a booking attempt is valid
    according to the requirements.
    Parameter: tsc - a dict format info passed by the
    frontend form inputs
    Return: a dict format info containing all column
    info needed to save the valid booking to db
    Exception: may raise InvalidBooking exception if
    requirements are violated.
    '''

    (balance, ) = Users.query.with_entities(Users.balance) \
        .filter_by(user_id=tsc["user_id"]).first()

    (user_id, price) = PropertyModel.query.with_entities(
        PropertyModel.user_id, PropertyModel.price
    ).filter_by(prop_id=tsc["prop_id"]).first()

    try:
        user_check_in_date = datetime.strptime(
            tsc["check_in_date"], "%Y-%m-%dT%H:%M")

        user_check_out_date = datetime.strptime(
            tsc["check_out_date"], "%Y-%m-%dT%H:%M")
    except ValueError:
        raise InvalidBooking("Invalid date format, please use YYYY-MM-DD")

    total_days = float((user_check_out_date - user_check_in_date).days)

    total_price = price * total_days

    # A user cannot book a listing that
    # costs more than his/her balance.
    if float(balance) < float(total_price):
        raise InvalidBooking("User can't afford the property")

    # A user cannot book a listing for his/her listing.
    if user_id == tsc["user_id"]:
        raise InvalidBooking("User can't book his own property")

    rows = TscModel.query.with_entities(
        TscModel.check_in_date, TscModel.check_out_date
    ).filter_by(property_id=tsc["prop_id"]).all()

    if rows is not None:
        for row in rows:
            (check_in_date, check_out_date) = row
            '''
            check_in_date       check_out_date
                C1----------------------C2
            
                    user_check_in_date         user_check_out_date
                        U1--------------------------------U2
                        
                    check_in_date       check_out_date
                        C1----------------------C2
            
            user_check_in_date         user_check_out_date
                U1----------------------------U2
                
            check_in_date                   check_out_date
            C1-----------------------------------C2
        
                user_check_in_date       user_check_out_date
                    U1----------------------U2
            '''

            # maybe buggy
            Overlap1 = check_out_date >= user_check_in_date \
                and check_out_date <= user_check_out_date
            Overlap2 = check_in_date >= user_check_in_date \
                and check_in_date <= user_check_out_date

            # reverse it,
            Overlap3 = user_check_out_date >= check_in_date \
                and user_check_in_date <= check_out_date
            Overlap4 = user_check_in_date >= check_in_date \
                and user_check_in_date <= check_out_date

            if Overlap1 or Overlap2 or Overlap3 or Overlap4:
                raise InvalidBooking("the selected date is overlapped")

    transaction = {
        **tsc
    }
    transaction["tsc_id"] = uuid.uuid4().hex
    transaction["tsc_date"] = datetime.now()
    transaction["tsc_price"] = total_price
    transaction["remaining_balance"] = float(balance) - float(total_price)

    return transaction


def save_transaction_record(tsc):
    '''
    This function saves the valid booking to the db.
    Parameter: tsc - savable booking in dict format
    Return: None
    Exception: rolls back and re-raises the database
    error if saving fails.
    '''
    try:
        db.session.add(TscModel(
            tsc_id=tsc["tsc_id"],
            user_id=tsc["user_id"],
            property_id=tsc["prop_id"],
            tsc_date=tsc["tsc_date"],
            tsc_price=tsc["tsc_price"],
            check_in_date=datetime.fromisoformat(tsc["check_in_date"]),
            check_out_date=datetime.fromisoformat(tsc["check_out_date"]),
            guest_number=tsc["guest_number"]))

        # reduce the balance here
        Users.query.filter_by(user_id=tsc["user_id"]).update(
            {"balance": tsc["remaining_balance"]})
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
