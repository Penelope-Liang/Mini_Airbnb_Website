# Scrum Board Sprint 6

meeting time: 2022.12.01

###Team Member 1:

**Name**:

Huilin Xu

**Branch**:

ship_meghan

**Progress**:

I'm trying to ship the whole system and will create the database web interface after successfully running docker, and then everything will be done. But before I do that, I need to solve the difficulties mentioned below.

**Difficulties**:

I'm having problems running docker desktop and it keeps saying "Docker Desktop starting...". I have reinstalled it many times and tried every method available on the stackoverflow, but nothing works. I haven't solved it yet, but I believe the dawn is near.

**Plan**:

Just now I managed to complete everything I needed for the assignment on another computer, but I still want to know why I can't run it on my own. So I will keep trying. Outside of that, I will comment positively on my teammate's pr and hope that this assignment will also wrap up well.

### Team Member 2:

**Name**:

Ximing Yu

**Branch**:

mybooking

**Progress**:

I added a new "My Bookings" page to show all the bookings a user has. The controller related to its actions is also done. For the frontend integration testing part, I have written tests covering the first three requirments.

**Difficulties**:

I encountered some difficulties when dealing with the "booking" functionality. I spent some time figuring out how to determine which property the user intends to book, as all properties are rendered on the same page and each is attached with a book button. In the end, we implemented a walk-around confirmation page to get the unique property id. Very fun work.

**Plan**:

There are still some details needed to be polished. Also, I will add more test cases for the integration testing, and work on the project deployment as soon as all other parts are finished.

### Team Member 3:

**Name**:

Yuanqi Liang

**Branch**:

test_sql_inj_createlisting

**Progress**:

I create the sql injection backend testing for create_listing function of each parameters and store the data in the correct format to the database and check whether there is any exception.

**Difficulties**:

I had difficulties with saving data to database, I have already finished the code of sql injection, but the data in the correct format did not store to the database.

**Plan**:

The plan is to continue fixing the problem of accessing to the database, since the function using the method of createlisting.py, it is possible that something wrong in createlisting.py and fix it, and back to sql injection check if it can work.

### Team Member 4:

**Name**:

Lu Chen, 18lc44, 20164422

**Branch**:

test_update_listing

**Progress**:

I have finished the backend of booking system, two functions are done, and testings are still little behind, and there might be some bugs

**Difficulties**:

The previous injection tests have some bugs, and this incur garbage data fluxs into data.db, it make this time hard to finish the test

**Plan**:

My plan is to clean up the db file, as the db now is full with garbage data, and also modify the pre-test and post-test session to let the test data in and out smoothly
