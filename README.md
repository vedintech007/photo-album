# Photo Storage App

This project is an inspiration from google photos

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

**Prerequisites**

```
Check requirements.txt for packages to install or follow along!
```

**Installations for mac and linux users**

```
First clone the repository from Github
```

* git clone https://github.com/Victorspy-web/photo-album.git


## Please Now Do This

**Create this file in the project base where settings.py can be found**

`SECRET_KEY.py `

* Inside the `SECRET_KEY.py`, create a variable name called SECRET_KEY and store your secret key in it. https://djecrety.ir can help you generate one.


```
Open terminal and install pipenv for your project
```

`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* sudo apt install pipenv

```
Install Django, activate and migrate project
```

* pipenv install django==3.2 . `Dont forget the space and dot at the end!`
* pipenv shell
* pip install Pillow
* pip install django-cleanup
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
