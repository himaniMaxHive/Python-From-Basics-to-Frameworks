# Basic implementation for any Django Project

Create a directory, and a virtual environment, from hereon in Virtual Environment
Install:
```
django
pillow
```

1. Create project 
```
django-admin startproject <project-name>
```
2. inside project, check it status by running the server
```
python manage.py runserver
```
3. Migrations steps
```
python manage.py makemigrations
python manage.py migrate
```
4. create superuser
```
python manage.py createsuperuser
# in terminal add your username, email (this can be empty), and password
```
5. For media and static config
- create `templates` and `static` at root level (same as in manage.py directory)
- in settings.py
```
import os 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media directory and it's path
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
- in urls.py
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #...
    #...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
6. Templates config
- inside settings.py 
```
'DIRS': ['templates'], # inside template section
```
7. create app
```
python manage.py startapp <app_name>
```
- inside app folder create: 
    - forms.py
    - urls.py (copy base structure from root directory urls.py)
- in settings.py (root level)
```
INSTALLED_APPS = [
    #,
    #,
    #,
    '<app_name>',
]
```
- inside urls.py (project level)
```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<app_name>/',include('<app_name>.urls'))
    #...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
`Notes`:
1. After creating model(s) remember to register it to Admin
2. Whenever working with django built-in user registration, actual UI (HTML) file will be at Root level template folder with different folder named `registration` and it will contain files `register.html`, `login.html` and `logged_out.html`.

