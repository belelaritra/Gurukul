<div align="center">
    <img src="static/images/Gurukul.png" height="300" alt="Gurukul Logo"/>
</div>
<h1 align="center"> Gurukul </h1>
<p align="center">
    <a href="https://github.com/belelaritra/Gurukul"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/belelaritra/Gurukul/issues">Report Bug</a>
    ·
    <a href="https://github.com/belelaritra/Gurukul/issues">Request Feature</a>
  </p>
</p>


<!-- ABOUT THE PROJECT -->

## About The Project:
<p>Gurukul is a e learning portal for RCCIITians.</p>


## Tech Stack:

<div align="center"><p>

![Dajngo](https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif)   
 
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)&nbsp;&nbsp;[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)&nbsp;&nbsp;[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
    </p></div>

## Clone The Project:
```
git clone https://github.com/belelaritra/Gurukul
```

## Installation:
- 1st Install `Django` on your machine.
- Then Install  other dependencies.
```
pip install -r requirements.txt
```
## Environment Setup
Before Starting the Server 
1. Create `.env` file inside root project directory.
2. Add `EMAIL` , `PASSWORD` and `SECRET_KEY` variables into `.env` file.
Like :
```
EMAIL = 
PASSWORD = 
SECRET_KEY = 
```
3. Give propper values to the variables & for `Password` enter the login password of your email.
> For `PASSWORD` :
- Turn on [`Allow less secure apps`](https://myaccount.google.com/lesssecureapps) to <b>ON</b> from [here](https://myaccount.google.com/lesssecureapps).

> For `SECRET_KEY` :
- Copy & run the following command in terminal.
```
django-admin startproject myproject
cd myproject/myproject
```
- Now open `settings.py` file and copy the `SECRET_KEY` value from line number `23`.

>Sample `SECRET_KEY` value : <br>`django-insecure-&)#p8aqf*r0pxv_ui2lxhxgax&@psu1@+jk9gi^vq3af0gqixi`
## Make Migration and Migrate:
```
python manage.py makemigrations
python manage.py migrate
```
## Run the server :
```
python manage.py runserver
```
Now you can access the server at `http://localhost:8000/`.