# Scrum Board Sprint 6

meeting time: 2022.12.03

###Team Member 1:

**Name**:

Huilin Xu

**Branch**:

mybookingV2.0

**Progress**:

I've done most of the work and fixed another bug in the middle of the progress where the user booked a different room than the one shows in mybooking. I also finished the testing part and confirmed that the booked listing will show up on the user's home page and a user cannot book a listing that is already booked with the overlapped dates.

**Difficulties**:

I couldn't test it at first and it kept showing that it couldn't connect to the database, then I realized that I had accidentally changed the code to link to the database when I changed the last bug. After that, everything went smoothly.

**Plan**:

My plan now is to relax and get myself a drink because our last assignment is wrapping up! Of course, since the prof gave the extension, we have more time to do a check to make sure we didn't write anything wrong.

### Team Member 2:

**Name**:

Ximing Yu

**Branch**:

mybookingV2.0

**Progress**:

The frontend development and testing are finished. I have PRed and it is reveiw and approved.

**Difficulties**:

I did not encounter much difficulties wrapping up the frontend dev&testing. However, I figured it did take me some time to recall how I programmed controller/tested with SeleniumBase/used Docker commands, even I just used them weeks ago. Practice makes perfect!

**Plan**:

Ship the container and the whole system :) Go over the final version to make sure we do not miss anything.

### Team Member 3:

**Name**:

Yuanqi Liang

**Branch**:

test_security4.0

**Progress**:

I finished the sql injection backend testing for booking function of each parameters and can sucessfully save the data in correct format into the database and check whether there is any exception.

**Difficulties**:

Even I write delete sql injection to delete the spam data and add connection.commit() to close the database, it doesn't work, the spam data can still save in database. I tested several times but cannot find the error.

**Plan**:

The plan is to continue fixing the problem, print the each line of data in databse and check whether it is SQL injection wrong, and fix the data.db.

### Team Member 4:

**Name**:

Lu Chen, 18lc44, 20164422

**Branch**:

test_update_listing

**Progress**:

I have fix a bug in the currenting booking test, but there are still some bugs in the previous security test, but these bugs are not triggered in previous tests, so I did not notice, but now they become a problem

**Difficulties**:

After cleaning off the garbage data in the data.db, some tests fail bc the changes in the database, I am still working on the reasons

**Plan**:

Fix all the tests that fail after the mass change in the data.db
