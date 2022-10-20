from qbay import app
from flask import render_template, request, session, redirect, url_for
from qbay.models import Users
from qbay.login import login_checker, login_saving
from qbay.register import register, register_format_checker, register_saving
from qbay.updateUserProfile import update_user_checker, update_user_saving
from qbay.exceptions import InvalidLogin
from qbay.db import db
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
            try:
                import os
                path = os.path.dirname(os.path.abspath(__file__))
                connection = sqlite3.connect(path + "/data.db")
                cursor = connection.cursor()
                row = cursor.execute(
                    "SELECT email FROM 'Users' WHERE email = email")
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


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = {
        "email": email,
        "password": password
    }
    try:

        login_checker(user)
        row = login_saving(user)
        if row:
            session['logged_in'] = row[0]
        return redirect('/', code=303)
    except:
        return render_template('login.html', message='login failed')


@app.route('/', endpoint='home')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    # some fake product data
    products = [
        {'name': 'prodcut 1', 'price': 10},
        {'name': 'prodcut 2', 'price': 20}
    ]
    return render_template('index.html', user=user, products=products)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
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
        # find a way to displat the exception msg?
        register_format_checker(user)
        reg_user = register_saving(user)
        print(reg_user)
        try:
            # query to check if user already exists?
            register(reg_user)
            print("yes")
        except:
            error_message = "Registration failed:("
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


"""
    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = r(name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')

"""


@app.route('/update_user', methods=['GET'])
def update_user_get():
    print("hello")
    email = session['logged_in']
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()
    row = cursor.execute("SELECT * FROM 'Users' WHERE email = email")
    user = cursor.fetchone()
    connection.close()
    print(user)
    session['id'] = user[0]
    if user:
        return render_template('update_user.html', user=user, message='connect')
    else:
        return render_template('update_user.html', message='failed')


@app.route('/update_user_save', methods=['GET'])
def update_user_get2():
    # templates are stored in the templates folder
    return render_template('update_user_save.html', message='Please Enter Info')


@app.route('/update_user_save', methods=['POST'])
def update_user_save():
    # templates are stored in the templates folder
    print("Yes")
    Email = request.form.get('email')
    if Email == "":
        print("dum dum")
    Password = request.form.get('password')
    Name = request.form.get('name')
    Billing_Address = request.form.get('billing_address')
    Postal_Code = request.form.get('Postal_Code')
    print("Yes2")
    user = {
        "acc_name": Name,
        "email": Email,
        "password": Password,
        "address": Billing_Address,
        "postal_code": Postal_Code
    }
    id = session['id']
    try:

        update_user_checker(user)
        update_user_saving(user, id)
        print("Yes3")
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        row = cursor.execute(
            "SELECT * FROM 'Users' WHERE user_id = (?)", (id,))
        user = cursor.fetchone()
        connection.close()
        print(user)
        if user:
            return render_template('update_user.html', user=user, message='connect')
    except:
        return render_template('update_user_save.html', message='login failed')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')
