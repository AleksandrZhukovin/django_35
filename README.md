# Launch the Project
Do the following steps to launch this project
1. Create and activate virtual environment. For that use your IDE (PyCharm etc.) 
or use `python -m venv .venv` & `.venv/scripts/activate` commands.
2. Install required libs from **_requirements.txt_** file with `pip install -r requirements.txt` command.
3. The project is set up. Use commands you need, modify code etc.

# Django Spreadsheet
## Start Project
- `pip install django`
- `django-admin startproject <your_project_name>` - start django project

## Project Actions
- `python manage.py startapp <your_app_name>` - start django application
- `python manage.py runserver` - run django server

## Migrations
- `python manage.py makemigrations` - create migrations files
- `python manage.py migrate` - run unapplied migrations files


## Admin
- `python manage.py createsuperuser`