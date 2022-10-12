'''
R5-1: One can update all attributes of the listing, except owner_id and last_modified_date.
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated when the update operation is successful.
R5-4: When updating an attribute, one has to make sure that it follows the same requirements as above.
'''

from datetime import datetime
#import models
import sqlite3

# listing (id, title, description, price, last_modified_date, owner_id)
# very similar to the update user profile


def check_title_format(title):
    '''
    para: corresponding type, benefits easier readable test cases
    return: bool
    '''
    return False


def check_description_format(description):
    return False


def check_price_range(price):
    return False


def check_last_modified_date(last_modified):
    return False


def check_owner_bg(owner_id):
    '''
    here check both existence and product's uniqueness
    '''
    return False


def format_checker(listing):
    '''
    call all check functions pass in list["title"]
    para: json
    return: bool
    '''
    return (check_title_format(listing["title"]) and check_description_format(listing["description"])
            and check_price_range(listing["price"]) and check_last_modified_date(listing["last_modified_date"])
            and check_owner_bg(listing["user_id"]))


def update_listing(user_id, prop_id, title, description, price, posted_date):
    '''
    Update existing listing
    '''

    print("Hello")

    # check id
    if id is None:
        return False

    # R5-2: Price can be only increased but cannot be decreased
    # if (models.PropertyModel.price > price):
        # return False

    #old_last_modified_date = models.PropertyModel.posted_date
    date = datetime.now()
    print(str(date))
    if not check_last_modified_date(date):
        return False

    # R5-4: When updating an attribute, one has to make sure that it follows the same requirements as above.
    title_check = check_title_format(title)
    description_check = check_description_format(description)
    price_check = check_price_range(price)

    check_update = True

    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/../../data.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT user_id, posted_date FROM Properties WHERE prop_id = (?)", (prop_id))
    rows = cursor.fetchone()
    print(rows)
    real_user_id = rows[0]
    real_date = rows[1]

    connection.close()
    
    if real_date is None:
        print("Ok")

    if real_user_id != user_id:
        return False

    # R5-1: One can update all attributes of the listing, except owner_id and last_modified_date.
    # if title_check and description_check and price_check:
        #models.PropertyModel.prop_id = prop_id
        #models.PropertyModel.title = title
        #models.PropertyModel.description = description
        #models.PropertyModel.price = price
        # return check_update

    # R5-3: last_modified_date should be updated when the update operation is successful.
    # last_modified_date = date
    last_modified_date = date
    # if check_update and (last_modified_date is not old_last_modified_date):
    #print("last modified date successfully update")
    # return True


if __name__ == '__main__':
    update_listing("20a7066e8e844759a99a20ecbd6935fe",
                   "59a99a20ecbd6935fe", "staffer", "Queens", 1000, datetime.now())
