# Chapter: 1
- Python command to run the test:
``` sh
python functional_tests.py
```
- The first step in getting Django up and running is to create a project, which will be the main container for our site.
- Django provides a little command-line tool for this:
```sh
django-admin startproject superlists .
```
- Don’t forget that "`.`" at the end; it’s important!
- That will create a file called manage.py in your current folder, and a subfolder called superlists, with more stuff inside it:
```sh
.
├── functional_tests.py
├── manage.py
└── superlists
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
- The superlists folder is intended for stuff that applies to the whole project—​like settings.py, for example, which is used to store global configuration information for the site.
- But the main thing is `manage.py`. That’s Django’s Swiss Army knife, and one of the things it can do is run a development server.
- Let’s try that now:
```sh
python manage.py runserver
```
- That’s Django’s development server now up and running on our machine.

---
# Chapter: 2

