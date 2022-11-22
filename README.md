# CISC327 - Group Project

![Examples tested with pytest-readme](https://img.shields.io/badge/pytest-passed-green)

![Examples tested with pytest-readme](https://img.shields.io/badge/style-passed-green)

```
│   .gitignore
│   A0-contract.md
│   data.db
│   db_init.sql
│   docker-compose.yml                          *A5 Submission
│   Dockerfile                                  *A5 Submission
│   LICENSE
│   pkg.txt
│   README.md
│   ScrumBoard_Screen_Shot.png
│   Sprint#4_ScrumUpdates.md
│   Sprint#5_ScrumUpdates.md                    *A5 submission
│   wait-for-it.sh
│
├───.github
│   │   pull_request_template.md
│   │
│   └───workflows
│           pytest_all.yml
│           style_check.yml
│
├───.vscode
│       settings.json
│
├───qbay
│   │   controllers.py
│   │   createListing.py
│   │   data.db
│   │   db.py
│   │   exceptions.py
│   │   login.py
│   │   models.py
│   │   regexRepo.py
│   │   register.py
│   │   updateListing.py
│   │   updateUserProfile.py
│   │   __init__.py
│   │   __main__.py
│   │
│   └───templates
│           base.html
│           create.html
│           createlisting_post.html
│           index.html
│           login.html
│           mine.html
│           register.html
│           updatelisting.html
│           updatelisting_save.html
│           update_user.html
│           update_user_save.html
│           update_user_style.html
│
└───qbay_test
    │   conftest.py
    │   pytest.init
    │   test_create_listing.py
    │   test_login.py
    │   test_register.py
    │   test_update_listing.py
    │   test_update_user.py
    │   __init__.py
    │
    ├───test_frontend
    │       test_createlisting.py
    │       test_dummy.py
    │       test_login.py
    │       test_register.py
    │       test_update_listing.py
    │       test_user_update.py
    │
    └───test_security                           *A5 Submission
            Generic_SQLI.txt
            test_createlisting_sql_inj.py
            test_register_sql_inj.py
```
