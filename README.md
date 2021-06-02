# Photo Storage App

This project is an inspiration from google photos

## Getting Started

**Prerequisites**

```
First clone the repository from Github
```

* git clone https://github.com/Victorspy-web/photo-album.git


`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* pip install pipenv


```
Run this to install dependancies `pip install -r requirements.txt`
```

```
Activate and migrate project
```

* pipenv shell
* python manage.py makemigrations
* python manage.py migrate


```
Create django superuser
```

* python manage.py createsuperuser
    * Fill in the fields to create a superuser `Passwords are invisble`


```
You can now run the development server
```

* python manage.py runserver
    * `Paste this link in your browser to run local server` http://127.0.0.1:8000
