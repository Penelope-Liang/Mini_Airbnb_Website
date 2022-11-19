#  Scrum Board Sprint 4 
meeting time: 2022.11.09

###Team Member 1:

**Name**:

Huilin Xu

**Branch**:

test_user_update2

**Progress**:

I have done all the work, first testing that the three web pages from login to update_user work correctly, including changing the user name and postal code. Second I tested that the password and image elements existed, and finally I added two tests to ensure that the user name and zip code were updated in the database. I have completed all the pep8 tests and comments as well.

**Difficulties**:


I struggled for a long time at first because I forgot to introduce the database, and I didn't realize that I couldn't run main and test at the same time because one of the ports would be occupied and therefore report an error. After that I had no more problems because seleniumbase really works well.

**Plan**:

The rest of my plan is to keep updating my code as the group encounters problems to make sure we can all fit together in the end. And to do more black box testing to make sure there are no bugs that I've overlooked. I may also continue to update my comments to improve them further.



### Team Member 2:

**Name**:

Ximing Yu


**Branch**:

test_reg


**Progress**:

I have created 3 test cases covering the cases where the registration is successful, unsuccessful for repeated email and unsuccessful for invalid username bound. I have managed to test using three different blackbox methods for these three cases, that is, output partition, input partition and input boundary.


**Difficulties**:

I had some difficulties setting up the seleniumbase at the beginning. Additionally, for the places where I need to access the database, I spent a lot of time trying to figure out what my db path is.


**Plan**:

In the next few days, I plan to add more test cases to cover all requirements from A2. Furthermore, I will add documentation along the way and keep making sure my code is also flake8 error-free.




### Team Member 3:

**Name**:

Yuanqi Liang

**Branch**:

test_createlisting


**Progress**:

I create test cases successful creating listing, title, descpition, address with wrong format and number of characters, and price with wrong range of number, also check whether the email is empty and title is repeated. In test cases, I use three blackbox testing including input partition, output partition and input boundary.


**Difficulties**:

I had difficulties with accessing to database, and also I am confused how to test posted_date since the posted_date has already set default for date.today() and repeated title.

**Plan**:

The plan is to continue fixing the problem of posted date and repeated title. Then I will add comment in code and check the pep8 format.

### Team Member 4:

**Name**:

Lu Chen, 18lc44, 20164422

**Branch**:

test_update_listing


**Progress**:

I have tests out all the requirements with 3 different testing methods, all done and passed all test as expected 

**Difficulties**:

I didn't encounter much difficulites, the only thing is I found the function is not properly in the update listing function, which confused me a bit but all good now


**Plan**:

My plan is to publish a template branch about how we test it , and we can take a look, then you guys can merge you branch to my and finally merge to the main



