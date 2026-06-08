# MiniBlog

A Django-based blogging application named `miniblog` with a single app `blogApp`.

## Project Structure

- `miniblog/` - Django project configuration
  - `manage.py` - Django command-line utility
  - `miniblog/` - project settings, URL configuration, WSGI/ASGI
  - `blogApp/` - blog application with models, views, templates, and admin setup
  - `templates/` - HTML templates for user and admin modules
  - `media/` - uploaded media files

## Features

- User signup and login
- Blog creation, editing, and viewing
- Admin panel with user and blog management
- User profile editing
- Media upload support

## Dependencies

This project uses Django 3.0 and MySQL as the database backend.

Recommended dependencies:

- `Django==3.0`
- `mysqlclient`

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install Django==3.0 mysqlclient
   ```

3. Configure the database in `miniblog/miniblog/settings.py` if needed:
   - `NAME`: database name
   - `USER`: database user
   - `PASSWORD`: database password

4. Apply migrations:
   ```bash
   python miniblog/manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python miniblog/manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python miniblog/manage.py runserver
   ```

7. Open the application in your browser:
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Notes

- `DEBUG` is enabled in development settings.
- Static files are served via `STATIC_URL = '/static/'`.
- Uploaded media files are stored in `media/`.
- The application currently uses MySQL by default.
