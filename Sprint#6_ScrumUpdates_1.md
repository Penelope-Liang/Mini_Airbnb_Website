# Scrum Board Sprint 6

meeting time: 2022.12.01

###Team Member 1:

**Name**:

Huilin Xu

**Branch**:

booking_frontend

**Progress**:

I worked with Ximing to complete the front-end page of booking in the library, which includes three sections, showing all the properties for the user to choose, the user confirmation page, and my_booking, which is the page where the user can view all their bookings. The front-end page now looks perfect and all functions are working properly.

**Difficulties**:

I couldn't get the program to run, and in the end I found out that I hadn't changed fetchone to fetchall, which resulted in the database only being able to fetch one row. Beyond that, we've been struggling to know exactly which one the user has clicked on in a page with 50 book buttons.After an afternoon of discussion and debugging, we were lucky enough to make it.

**Plan**:

The rest of my task is to finish writing the testing part and make sure it can run correctly. After everyone has done their part, we will do another round of checking.

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

test_booking3.0

**Progress**:

I create the sql injection backend testing for booking function of each parameters and try to store the data in the correct format to the database and check whether there is any exception.

**Difficulties**:

I had difficulties with connect to database, I have already finished the code of sql injection, the data did not save in the database in correct format.

**Plan**:

The plan is to figure out how to fix the problem, and debug by each line to find the reason why cannot connect to the database.

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
