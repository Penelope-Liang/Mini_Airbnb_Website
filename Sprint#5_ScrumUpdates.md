# Scrum Board Sprint 5

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

template_yu

**Progress**:

I copied the provided template to our repo and made some changes accroding to our own file structure and configuations. I published a container of our app to the dockerhub following the instructions.

**Difficulties**:

I did not encounter much difficulties shipping the container, thanks to the detailed instructions given. But I did spend some time figuring out how to setup Docker and Dockerhub and learning how to use Docker. Very fun experience so far.

**Plan**:

In the coming days, I will test if the application can actually be pulled and run successfully from other machines. I may kindly ask my teammates to help test it lol :)

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

I have finished testing the sql injection of register, but injection for creating list still haven't done, I also switched it from using selenuim to directly calling the backend functions

**Difficulties**:

I used the selenium for testing at first and it is way too slow, and then I realize directly calling will be much more faster, it took me awhile to realize that

**Plan**:

My plan is to give out a template about how we testing and then if any vulnerabilities are found, we fix it, and also evaluate the performance as well.
