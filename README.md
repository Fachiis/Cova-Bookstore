****Cova Bookstore Application****
-
> This is an online bookstore application that allows registered authors of books to upload their books to the public for ease of purchase.
## Features

- Django 3.2, Python 3.7, Docker 3.7, Django-allauth 0.45.0, Strip 2.60.0, & Paystack
- Install via [Pipenv](https://pypi.org/project/pip/)
- User registration, log in/out, password change & password reset
- Upload a book by the authenticated author
- Edit uploaded book by the authenticated author
- Remove a book by the authenticated author
- List all available books
- Drop reviews on a book(s)
- Purchase a book
- Search for a book

The code style used for the project is PEP 8 -- Style Guide for Python Code and Flake8: For Style Guide
Enforcement.

---
## Table of Contents
* **[Installation](#installation)**
  * [Pipenv](#pip)
* [Setup](#setup)

---
## Installation
The application can be installed via Pipenv. To start,
clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Fachiis/Cova-Bookstore
$ cd Cova-Bookstore
```
```
$ python3 -m venv Cova-Bookstore
$ source Cova-Bookstore/bin/activate
(Cova-Bookstore) $ pipenv install --ignore-pipfile
(Cova-Bookstore) $ python manage.py migrate
(Cova-Bookstore) $ python manage.py createsuperuser
(Cova-Bookstore) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000/
```

## Setup

```
# Run Migrations
(Cova-Bookstore) $ python manage.py migrate

# Create a Superuser
(Cova-Bookstore) $ python manage.py createsuperuser

# Confirm everything is working:
(Cova-Bookstore) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000/
```
