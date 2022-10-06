'''
R3-1: A user is only able to update his/her user name, user email, billing address, and postal code.
R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
R3-3: Postal code has to be a valid Canadian postal code.
R3-4: User name follows the requirements above.
'''

'''
define your function here, and feed them with the data
call function inside the if __name__ == "__main__":
'''

if __name__ == "__main__":
    from regexRepo import *
    from exceptions import *

    '''
    attention, this function requires some pre-stored data
    in the database, you can run command [in the directory of backend]
    py ./resources/tools/register.py 
    '''

    # this user wants to update his address and postal code
    user_update1 = {
        "acc_name": "Saul Goodman",
        "first_name": "Jimmy",
        "last_name": "Mcgill",
        "email": "JimmyMcgill@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
        "postal_code": "L3S4V8"
    }

else:
    from .regexRepo import *
    from .exceptions import *
