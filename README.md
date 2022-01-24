<div align="center">
    <img src="static/images/Gurukul.png" href="https://gurukul-rcciit.herokuapp.com/" height="300" alt="Gurukul Logo"/>
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

## Tech Stack:
<div align="right">

[![Website monip.org](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)](https://gurukul-rcciit.herokuapp.com/)
[![Size](https://github-size-badge.herokuapp.com/belelaritra/Gurukul.svg)](https://github.com/belelaritra/Gurukul)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![django](https://img.shields.io/badge/django-3.8.10-092E20.svg)](https://pypi.org/project/Django/3.2.10/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/belelaritra/Gurukul)

</div>

<div align="center"><p>

![Dajngo](https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif)   
 
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)&nbsp;&nbsp;[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)&nbsp;&nbsp;[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
    </p></div>

<!-- ABOUT THE PROJECT -->
---
## About The Project:
<p><a href="https://gurukul-rcciit.herokuapp.com/"></a>Gurukul</a> is an E-learning portal for RCCIITians. Where user can ask questions and get answers from the community of RCCIITians, download E-books from the Digital Library, and much more.

The project is developed by a team of four students of RCCIIT as a part of their 3rd semester python project. 
#### Team members are:
- <img src="static/img/team/team-1.jpeg" height="20" style="border-radius:50%" alt="Aritra Belel"/>&nbsp;&nbsp;<a href="https://github.com/belelaritra"><strong>Aritra Belel</strong></a>
- <img src="static/img/team/team-2.jpeg" height="20" style="border-radius:50%" alt="Ankit Malakar"/>&nbsp;&nbsp;<a href="https://github.com/ankitmalakar7"><strong>Ankit Malakar</strong></a>
- <img src="static/img/team/team-3.png" height="20" style="border-radius:50%" alt="Soham Banerjee"/>&nbsp;&nbsp;<a href="https://github.com/soham4abc"><strong>Soham Banerjee</strong></a>
- <img src="static/img/team/team-4.jpeg" height="20" style="border-radius:50%" alt="Soham Sarkar"/>&nbsp;&nbsp;<a href="https://github.com/smart-worker"><strong>Soham Sarkar</strong></a>
</p>

---

### Clone The Project:
```
git clone https://github.com/belelaritra/Gurukul
cd Gurukul
```

### Installation:
- To install `Django` and other dependencies on your machine run this command.
```
pip install -r requirements.txt
```
### Environment Setup
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
### Make Migration and Migrate:
```
python manage.py makemigrations
python manage.py migrate
```
### Run the server :
```
python manage.py runserver
```
Now you can access the server at `http://localhost:8000/`.

---

## Features:
- Account:
    - Login & Signup
    - Email Verification
    - Forgot Password
    - Update Profile Picture
    - Edit Profile & Change Password
    - 3 time login attempts
    - Safe Mode

- Question:
    - Ask Question
    - Answer Question
    - Like & Dislike
    - Edit & Delete Question/Answer
    - Realtime Views count
    - Search Question
    - Filter Questions according to the tags
    - Sort Questions on the basis of time/views/likes/answers
    - Markdown Support 
    - Profinity Filter (Forbidden words will be replaced with `*`, if safe mode is on)

- Library:
    - Add Books
    - Preview Books
    - Download Books