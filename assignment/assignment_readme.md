## Django Assignment

### Tech Stacks Used

- Python as the primary language.
- Django and Django REST Framework for designing and executing APIs.
- PostgreSQL as a better database system

### Project Setup

- **Installing dependencies**

  - `pip install poetry`
  - `poetry install` : This will install all the required dependencies from .toml file.

- **Making database migrations**

  - `python manage.py makemigrations`
  - `python manage.py migrate`

- **Creating Superuser**

  - `python manage.py createsuperuser` : This will allow the user to have the access to admin pannel

- **Running the Django server**

  - `python manage.py runserver`

- **Adding Team Options**
  - POST request on `http://127.0.0.1:8000​/profile​/team​/` can add team options from Development, Product, Design and Human Resource.

### Swagger Documentation

- For proper understaning of API's usage, visit `http://127.0.0.1:8000/schema/`
- \***\*NOTE: To use the APIs, backend requires user to be authenticated. So, create an auth token, on `http://127.0.0.1:8000/app/login/` or `http://127.0.0.1:8000/app/register/`, from admin pannel for the access\*\***
