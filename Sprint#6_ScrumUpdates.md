# Scrum Board Sprint 5

meeting time: 2022.11.09

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

My plan is to give out a template about how we testing and then if any vulnerabilities are found, we fix it.
