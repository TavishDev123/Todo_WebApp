## DJANGO TO-DO App

A simple web-based To-Do list application built with Django.

Features:-
User authentication (Registration, Login, Logout)
Create, update, delete, and view tasks
Task completion tracking
Personalized task management per user

Prerequisites:-
Before you begin, ensure you have the following installed:

Python 3.x
pip (Python package installer)
Git (optional but recommended)

## Setup Instructions

1. Clone the Repository
bash
git clone https://github.com/your-username/todo_app.git
cd todo_app


2. Create a Virtual Environment
#bash
python -m venv venv
Activate the virtual environment:

On Windows:
#bash
venv\Scripts\activate
On macOS/Linux:
#bash
source venv/bin/activate


3. Install Dependencies
Install the required Python packages by running:
#bash
pip install -r requirements.txt


4. Set Up Environment Variables
Create a .env file in the root directory of the project and add the following variables:

#bash
SECRET_KEY='django-insecure-s^^r4egfndie7i!1ac0yu%h*%zsc($j-k2xk$t(i)s&#hluv=6'
DEBUG=True
ALLOWED_HOSTS=to-do-list-webapp-8k0i.onrender.com
DB_ENGINE='django.db.backends.sqlite3'
DB_NAME='db.sqlite3'


5. Apply Database Migrations
Run the following command to create the necessary database tables:

#bash
python manage.py migrate


6. Create a Superuser
To access the Django admin and manage tasks:
#bash
python manage.py createsuperuser


7. Run the Development Server
You can start the server using:
#bash
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the app.

8. Hosting (Render.com)
To host on Render.com:

Set your Root Directory to the todo_app directory if your manage.py file is located inside.
Set the Build Command to:
#bash
pip install -r todo_app/requirements.txt

Set the Start Command to:
#bash
gunicorn todo_app.wsgi:application

Make sure to update the ALLOWED_HOSTS in your .env file or environment variables on Render to include the Render app's domain.
Add environment variables from.env file.

If you're deploying the app and using a production environment, remember to run:
#bash
python manage.py collectstatic

