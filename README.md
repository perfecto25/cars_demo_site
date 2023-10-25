# Cars demo CRUD site with Django, HTMX, django-allauth

Youtube link to tutorial:




## initial setup

    django-admin startproject cars

cd cars

    pipenv install django django-allauth loguru
    pipenv shell
    django-admin startapp main

## generate SQLite DB

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser

open cars/settings.py add 'main' to Installed Apps

## Models and Forms

create new Cars model and CarsForm, register car model in Admin console view

## Django AllAuth

open cars/settings.py

update AUTHENTICATION_BACKENDS, INSTALLED_APPS, MIDDLEWARE, AllAuth config settings

makemigrations, migrate


to customize AllAuth pages (login, logout, reset password, etc)

copy page from site-packages directory to your templates/account directory

    cp /path/to/allauth/site-package/templates/account/logout.html main/templates/account/

