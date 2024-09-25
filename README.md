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

# 1. Clone the Repository: <br/>
bash<br/>
git clone https://github.com/your-username/todo_app.git
cd todo_app


# 2. Create a Virtual Environment:<br/>
bash<br/>
python -m venv venv<br/>
Activate the virtual environment:

On Windows:<br/>
bash<br/>
venv\Scripts\activate<br/>
On macOS/Linux:<br/>
bash<br/>
source venv/bin/activate


# 3. Install Dependencies:<br/>
Install the required Python packages by running:<br/>
bash<br/>
pip install -r requirements.txt


# 4. Set Up Environment Variables:<br/>
Create a .env file in the root directory of the project and add the following variables:<br/>

bash<br/>
SECRET_KEY='django-insecure-s^^r4egfndie7i!1ac0yu%h*%zsc($j-k2xk$t(i)s&#hluv=6'<br/>
DEBUG=True<br/>
ALLOWED_HOSTS=to-do-list-webapp-8k0i.onrender.com<br/>
DB_ENGINE='django.db.backends.sqlite3'<br/>
DB_NAME='db.sqlite3'<br/>


# 5. Apply Database Migrations:<br/>
Run the following command to create the necessary database tables:<br/>

bash<br/>
python manage.py migrate


# 6. Create a Superuser:<br/>
To access the Django admin and manage tasks:<br/>
bash<br/>
python manage.py createsuperuser


# 7. Run the Development Server
You can start the server using:<br/>
bash<br/>
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the app.

# 8. Hosting (Render.com)
To host on Render.com:<br/>

Set your Root Directory to the todo_app directory if your manage.py file is located inside.<br/>
Set the Build Command to:<br/>
bash<br/>
pip install -r todo_app/requirements.txt

Set the Start Command to:<br/>
bash<br/>
gunicorn todo_app.wsgi:application

Make sure to update the ALLOWED_HOSTS in your .env file or environment variables on Render to include the Render app's domain.<br/>
Add environment variables from.env file.<br/>

If you're deploying the app and using a production environment, remember to run:<br/>
bash<br/>
python manage.py collectstatic

