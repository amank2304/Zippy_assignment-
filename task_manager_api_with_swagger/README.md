# Task Manager API (Django + DRF)

## Setup Instructions

1.Open an terminal and run "git clone then https://github.com/amank2304/Zippy_assignment-.git" or simply download the repo and follow the rest steps.
2. Create virtual environment:
   python -m venv venv
   source venv/Scripts/activate (Windows)
3. Install requirements:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create superuser (To create Admin role):
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver

## API Documentation

Swagger UI:
http://127.0.0.1:8000/swagger/
1. Use register to register as an normal user
2. then with the credential login as an normal user
3. use the access token to get authorized 
4. in authorized put "Bearer <access_token>"
5. Now you can use every api (get, post, put, delete)
6. Use post task/  to generate an task for an logged in user
7. Use get task/ to get all tasks of an logged in user
8. Use get task/{id}/ to get a specific task of an logged in user
9. Use put task/{id}/ to update a specific task of an logged in user
10. Use delete task/{id}/ to delete a specific task of an logged in user
11. if you get authenticated with an admin credential and admin access token.
12. You can see all the tasks of all users in the system and also you can delete any task of any user.
13. you can also edit task of any user with an task id


Admin Site-
http://127.0.0.1:8000/admin/

1.Login with superuser credentials created in step 4.
2.You can create a user change it's information and also deactivate any user.

