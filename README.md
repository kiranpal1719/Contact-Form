# Contact Form - Django Project

## About This Project
A simple Contact Form built with Django where users can submit
their name, email, subject and message.

## Features
- Contact form with validation
- Messages saved in database
- View all messages in admin panel

## Project Structure
CONTACTFORM/
├── contact/
│   ├── templates/
│   │   └── contact/
│   │       └── contact.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── contactform/
│   ├── settings.py
│   ├── urls.py
└── manage.py

## Installation

### 1. Clone Repository
git clone <repository-url>
cd contactform

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install django

### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser
python manage.py createsuperuser

### 6. Run Server
python manage.py runserver

## URLs
- Contact Form : http://127.0.0.1:8000/
- Admin Panel  : http://127.0.0.1:8000/admin/

## Technologies Used
- Python
- Django
- SQLite
- HTML & CSS


