# Scrum Board Sprint 6

meeting time: 2022.12.03

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

I have fix a bug in the currenting booking test, but there are still some bugs in the previous security test, but these bugs are not triggered in previous tests, so I did not notice, but now they become a problem

**Difficulties**:

After cleaning off the garbage data in the data.db, some tests fail bc the changes in the database, I am still working on the reasons

**Plan**:

Fix all the tests that fail after the mass change in the data.db
