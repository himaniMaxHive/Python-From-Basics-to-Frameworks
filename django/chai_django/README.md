# Chai Aur Django

This project was built while learning from a YouTube course.

## 📚 Learning Resource

- **Course:** [Chai Aur Django](https://youtu.be/j6szNSzw4BU?si=ooeNjUqWS1RZaPiq)  
- **Instructor:**  [Hitesh Chaudhary](https://hitesh.ai/)
- **Platform:** [YouTube](https://youtu.be/j6szNSzw4BU?si=ooeNjUqWS1RZaPiq)
- **Link:** https://youtu.be/j6szNSzw4BU?si=ooeNjUqWS1RZaPiq

## 🧠 What I Learned
- Django project structure
- Models, Views, Templates
- Forms and URL routing

## ⚠️ Disclaimer
This project is created for **learning purposes**.  
The code is written by me while following the tutorial, with some personal modifications.


# Beginner-friendly list of the basic Django commands
### **[Below commands are from ChatGPT](https://chatgpt.com/share/694937e7-b750-8006-9ae9-46a9e140ec06)**

**1️⃣ Creating & Running a Django Project**
- ***Create a Django project***
    ``` 
    django-admin startproject projectname
    ```
    Creates the main Django project structure.

    📁 Structure:
    ```
    projectname/
    ├── manage.py
    └── projectname/
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
    ```
- ***Run the development server***
    ```
    python manage.py runserver
    ```
    Runs the app locally at:
    ```
    http://127.0.0.1:8000/
    ```
    Custom port:
    ```
    python manage.py runserver 8080
    ```

**2️⃣ Creating & Managing Apps**
- ***Create an app***
    ```
    python manage.py startapp appname
    ```
    📁 App structure:
    ```
    appname/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    └── migrations/
    ```
    📌 After creating an app, add it to INSTALLED_APPS in settings.py.

**3️⃣ Database & Migrations**
- ***Create migration files***
    ```
    python manage.py makemigrations
    ```
    Detects model changes and prepares database instructions.

- ***Apply migrations to database***
    ```
    python manage.py migrate
    ```
    Creates/updates tables in the database.

- ***Show migrations***
    ```
    python manage.py showmigrations
    ```

- ***Reset database tables (advanced)***
    ```
    python manage.py migrate appname zero
    ```

**4️⃣ Django Shell (Very Important)**
- ***Open Django interactive shell***
    ```
    python manage.py shell
    ```
    Use it to:
    - Test models
    - Query database
    - Debug logic
    
    Example:
    ```
    from app.models import User
    User.objects.all()
    ```

**5️⃣ Admin Panel Commands**

- ***Create superuser (admin login)***
    ```
    python manage.py createsuperuser
    ```
    You’ll be asked for:
    - Username
    - Email
    - Password
    Admin panel:
    ```
    http://127.0.0.1:8000/admin/
    ```

**6️⃣ Static Files & Templates**

- ***Collect static files (for production)***
    ```
    python manage.py collectstatic
    ```
    Copies all static files into one folder.

**7️⃣ Project Utilities**

- ***Check project for errors***
    ```
    python manage.py check
    ```

- ***List all available Django commands***
    ```
    python manage.py help
    ```
    Specific command help:
    ```
    python manage.py migrate --help
    ```

**8️⃣ Testing**

- ***🔹 Run tests***
    ```
    python manage.py test
    ```
    Run tests for a specific app:
    ```
    python manage.py test appname
    ```

**9️⃣ Database Inspection**
- ***View SQL for migrations***
    ```
    python manage.py sqlmigrate appname 0001
    ```

- ***🔹 Flush database (⚠ deletes data)***
    ```
    python manage.py flush
    ```

**🔟 Custom Commands (Advanced)**

- ***You can create your own commands:***
    ```
    python manage.py yourcommand
    ```
    📁 Location:
    ```
    app/
    └── management/
        └── commands/
            └── yourcommand.py
    ```

# manage.py vs django-admin

## What is `django-admin`?
**📌 Definition**

`django-admin` is a global Django command-line tool.

It is used to:
- Create Django projects
- Run Django commands without depending on a specific project

**📌 Key points**
- Installed when you install Django
- Works outside any Django project
- Does NOT automatically know your project settings

**📌 Use `django-admin` when:**
- Creating a new project
- Working outside a project directory

**Example:**
```
django-admin startproject blog
```

## What is `manage.py`?
**📌 Definition**

`manage.py` is a project-specific command wrapper.

It is used to:
- Is created inside every Django project
- Knows your project’s `settings.py`
- Automatically sets:
    ```
    DJANGO_SETTINGS_MODULE
    ```

**📌 Use `manage.py` when:**
- Running the server
- Running migrations
- Creating superusers
- Using shell
- Running tests

**Example:**
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```