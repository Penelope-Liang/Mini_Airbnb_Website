from datetime import date
from qbay import app
from flask import render_template, request, session, redirect

from qbay.booking import booking_requirement_checking, save_transaction_record
from qbay.exceptions import InvalidLogin, InvalidRegister
from qbay.exceptions import InvalidUserUpdate, InvalidBooking
# flask.url_for
# from qbay.models import Users
from qbay.login import login_checker, login_saving
from qbay.register import register, register_format_checker, register_saving
from qbay.updateListing import updateInfo, \
    update_listing_format_checker_1, updating_data
from qbay.updateUserProfile import update_user_checker, update_user_saving
# from qbay.exceptions import InvaildRegister  # InvalidLogin
from qbay.createListing import create_listing_format_checker, createlisting
from qbay.createListing import listing_saving
# from qbay.db import db
import sqlite3


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            print(email)  # for testing
            try:
                # link the database to select user's email
                import os
                path = os.path.dirname(os.path.abspath(__file__))
                connection = sqlite3.connect(path + "/data.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM 'Users' "
                               "WHERE email = (?)", (email,))
                # print(row)  # for testing
                # if found the email, store into user
                user = cursor.fetchone()
                connection.close()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                print(Exception)
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


# This function is used to connect the login.html
@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


# This function is used to get user information on the web
# check if the user can login based on the database
@app.route('/login', methods=['POST'])
def login_post():
    # get email and password
    email = request.form.get('email')
    password = request.form.get('password')

    # login checker input -> dic
    user = {
        "email": email,
        "password": password
    }

    # if info enter by user pass all the test below, user log in, else, fail
    try:
        login_checker(user)  # check the format

        # store the user email and password in row if find
        row = login_saving(user)
        print('denglu {}'.format(row))
        if row != "None":
            # set the session logged_in to user's email
            session['logged_in'] = row[0]
        return redirect('/', code=303)
    except InvalidLogin as IL:
        return render_template('login.html',
                               message=IL.message)


@app.route('/', endpoint='home')
@authenticate
def home(user):
    '''
    This function is used to show the home page once user log in
    '''
    print(user)
    try:
        # link the database to fetch all properties
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM 'Properties' WHERE user_id = (?);", (user[0],))
        all_prod = cursor.fetchall()
        connection.close()
        return render_template('index.html', user=user,
                               products=all_prod, message="")
    except Exception:
        # if there has been any error loading properties, display err msg
        return render_template('index.html', user=user, products=[],
                               message="Soory! There has been \
                                an error loading the products")


@app.route('/register', methods=['GET'])
def register_get():
    '''
    This function is to get the register page for display
    '''
    return render_template('register.html', message=" ")


@app.route('/register', methods=['POST'])
def register_post():
    '''
    This function is to handle the post action on the register page
    '''
    # get all user inputs
    email = request.form.get('email')
    acc_name = request.form.get('name')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # if two passwords do not match, set error msg
    if password != password2:
        error_message = "The passwords do not match"
    else:
        user = {
            "acc_name": acc_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        try:
            # check if inputs have any format error
            register_format_checker(user)
            reg_user = register_saving(user)
            # register the new user to the database
            register(reg_user)
        # pass the customized exception err massage to var error_message
        # if there is any
        except InvalidRegister as err:
            error_message = f"{err.message}"
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/update_user', methods=['GET'])
def update_user_get():
    """
    This function is used to find all the information of a user
    and shows on update_user.html
    """

    email = session['logged_in']  # get the email from session stored above
    print(email)  # for testing
    # connect the database
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()

    # select all the info of the user
    row = cursor.execute("SELECT * FROM 'Users' WHERE email = (?)", (email,))
    print(row)  # for testing
    user = cursor.fetchone()
    connection.close()
    print(user)

    # store another session which is id
    session['id'] = user[0]

    # if fetch success, return user info on the web
    if user:
        return render_template('update_user.html',
                               user=user, message='connect')
    else:
        return render_template('update_user.html',
                               message='failed')


# This function is to connect user
# to update_user_save.html if they click on update
@app.route('/update_user_save', methods=['GET'])
def update_user_get2():
    # templates are stored in the templates folder
    return render_template('update_user_save.html',
                           message='Please Enter Info')


"""
This function is used to update all the information user entered
and re-shows everything update to them
"""


@app.route('/update_user_save', methods=['POST'])
def update_user_save():
    # templates are stored in the templates folder
    # get all the info enter from web
    Email = request.form.get('email')
    Password = request.form.get('password')
    Name = request.form.get('name')
    Billing_Address = request.form.get('billing_address')
    Postal_Code = request.form.get('Postal_Code')

    # store in a dic so it can be used as input
    user = {
        "acc_name": Name,
        "email": Email,
        "password": Password,
        "address": Billing_Address,
        "postal_code": Postal_Code
    }
    id = session['id']

    # if update success, return back to update_user.html, else, fail
    try:
        update_user_checker(user)  # check the format
        update_user_saving(user, id)  # check the database

        # connect the database
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()

        # select all the info based on user id
        row = cursor.execute("SELECT * FROM 'Users' "
                             "WHERE user_id = (?)", (id,))
        print(row)  # for testing
        user = cursor.fetchone()  # store info fetch into user
        connection.close()
        if user:
            return render_template('update_user.html', user=user,
                                   message='Hi!Below is your Information')
    except InvalidUserUpdate as IUU:
        return render_template('update_user_save.html',
                               message=IUU.message)


# log out of the web
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


@app.route('/create', methods=['GET'])
def createlisting_get():
    return render_template('create.html',
                           message='Let\'s Start Creating Listing')


@app.route('/create', methods=['POST'])
def createlisting_post():
    email = session['logged_in']
    prop_id = request.form.get('prop_id')
    user_id = request.form.get('user_id')
    # posted_date = request.form.get('date')
    title = request.form.get('title')
    description = request.form.get('description')
    img = request.form.get('img')
    price = request.form.get('price')
    address = request.form.get('address')
    capacity = request.form.get('capacity')

    listing = {
        "email": email,
        "prop_id": prop_id,
        "user_id": user_id,
        "posted_date": date.today(),
        "title": title,
        "description": description,
        "img": img,
        "price": price,
        "address": address,
        "capacity": capacity
    }

    create_listing_format_checker(listing)
    new_listing = listing_saving(listing)
    try:
        createlisting(new_listing)
        return render_template(request, '/createlisting_post.html',
                               message='Create listing fail')
    except Exception:
        return render_template('createlisting_post.html', data=listing)


@app.route('/create', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return render_template(request, '/createlisting_post.html',
                           message='Create picture')


@app.route('/updatelisting', methods=['GET'])
def updatelisting_get():
    prop_id = request.args.get('prop_id')
    return render_template('updatelisting.html', data=prop_id,
                           message='Let\'s Start Update Listing')


@app.route('/updatelisting', methods=['POST'])
def updatelisting_post():
    email = session['logged_in']
    prop_id = request.form.get('prop_id')
    title = request.form.get('title')
    description = request.form.get('description')
    image = request.form.get('img')
    price = request.form.get('price')
    address = request.form.get('address')
    capacity = request.form.get('capacity')

    updatelisting = {
        "email": email,
        "prop_id": prop_id,
        "title": title,
        "description": description,
        "image": image,
        "price": price,
        "address": address,
        "capacity": capacity,
    }

    if prop_id:
        update_listing_format_checker_1(updatelisting)
        new_prop = updating_data(updatelisting)
        print("update")
        try:
            updateInfo(new_prop)
            return render_template('updatelisting_save.html',
                                   data=new_prop)

        except Exception:
            return render_template(request, '/updatelisting_save.html',
                                   message='Update listing fail')

    else:
        print("insert")
        create_listing_format_checker(updatelisting)
        new_listing = listing_saving(updatelisting)
        try:
            createlisting(new_listing)
            return render_template('updatelisting_save.html',
                                   data=updatelisting)

        except Exception:
            return render_template(request, '/updatelisting_save.html',
                                   message='Update listing fail')


@app.route('/mine', methods=['GET'])
def myProperties():
    try:
        # check the user
        email = session['logged_in']
        print('current_user {}'.format(email))
        # get the email from session stored above
        # connect the database
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()

        sql = 'select * from Users where email = "%s"' % (email)
        cursor.execute(sql)
        user = cursor.fetchone()
        print(user)
        user_id = user[0]
        connection.close()

        # use user_id to check properties
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        sql = 'select * from Properties where user_id="%s"' % (user_id)
        cursor.execute(sql)
        all_prod = cursor.fetchall()
        connection.close()
        prop_id = request.args.get('prop_id')
        return render_template('mine.html', user=user,
                               products=all_prod, message="")

    except Exception as e:
        print(e)
        # if there has been any error loading properties, display err msg
        return render_template('index.html', user=user, products=[],
                               message="Soory! There has been \
                                an error loading the products")


@app.route('/Booking', methods=['GET'])
def booking_get():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()
    # select all the info of the user
    row = cursor.execute("SELECT * FROM 'Properties'")
    properties = cursor.fetchall()
    connection.close()

    return render_template('Booking.html', properties=properties,
                           message='show properties')


@app.route('/conformation', methods=['GET'])
def conformation_get():
    prop_id = request.args.get('prop_id')
    print(prop_id)
    return render_template('conformation.html', prop_id=prop_id,
                           message=" ")


@app.route('/conformation', methods=['POST'])
def conformation_post():
    print("hihi")
    prop_id = request.args.get('prop_id')
    email = session['logged_in']
    print(email)
    print("^^^^^^^^^^^^^^^^^")
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()
    sql = 'select * from Users where email = "%s"' % (email)
    cursor.execute(sql)
    user = cursor.fetchone()
    print(user)
    id = user[0]
    print(id)
    connection.close()

    Date = request.form.get('date')
    Date += "T00:00"
    print(Date)
    Date2 = request.form.get('date2')
    Date2 += "T00:00"
    print(Date2)
    number = request.form.get('guest_number')
    print(number)
    err_msg = None
    tsc = {
        "user_id": id,
        "prop_id": prop_id,
        "check_in_date": Date,
        "check_out_date": Date2,
        "guest_number": number
    }

    try:
        tsc_new = booking_requirement_checking(tsc)  # check the format
        print("PASSSSSSS")
        save_transaction_record(tsc_new)
        print("ahhhhhhhhhh book it already!!!!!!!!!")
    except InvalidBooking as IUU:
        err_msg = f"{IUU.message}"
    if err_msg:
        return render_template('conformation.html',
                               message=err_msg)
    else:
        return redirect('/')


@app.route('/my_booking', methods=['GET'])
def booking_get2():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()
    id = session['id']
    print(id)
    # select all the info of the user
    row = cursor.execute("SELECT * FROM 'Transactions' "
                         "WHERE user_id = (?)", (id,))
    bookings = cursor.fetchall()
    connection.close()
    prop_id = request.args.get('prop_id')
    # templates are stored in the templates folder
    return render_template('my_booking.html', bookings=bookings, data=prop_id,
                           message='Please Enter Info')
