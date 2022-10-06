'''
R4-1: The title of the product has to be alphanumeric-only,
      and space allowed only if it is not as prefix and suffix.
R4-2: The title of the product is no longer than 80 characters.
R4-3: The description of the product can be arbitrary characters, 
      with a minimum length of 20 characters and a maximum of 2000 characters.
R4-4: Description has to be longer than the product's title.
R4-5: Price has to be of range [10, 10000].
R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
R4-7: owner_email cannot be empty. The owner of the corresponding 
      product must exist in the database.
R4-8: A user cannot create products that have the same title.
'''
from datetime import date


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

    # we don't have last_modify date, but I think you can use posted_date
    proerpty_1 = {
        "title": "A delighted mansion",
        
        "description": "This is a mansion sits beside a beach with 16hr+ " +
        "sunshine, beside daily facillities also" +
        "provide with mini swimming pool",
        
        "price": 5000,
        "email": "JimmyMcgill@SGA.com",
        "posted_date": date.today(),
        "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
        "postal_code": "L3S4V8"
    }

else:
    from .regexRepo import *
    from .exceptions import *
