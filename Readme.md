# Django Notes

- **UV** : There is a package maneger which is very fast in process. To install it on Linux: ```pip3 install uv```
  
- **Create virtual enviroment** : It was very easy to create venv in python useing uv. The command is ``` uv venv```  and to activate the venv by useing this command in Linux: ```source .env/bin/activate```
  
- **Install Django** : To install Django in venv useing uv by useing this command: ```uv pip install Django```
  
- **Create Django Project** : First we need to create a project useing django with help of this command: ```django-admin startproject <projectName>```. Here django-admin command is available after Django installation and startproject create the project with help of the projectName(anything given by us). After creating the project there will be a folder with the name as given in projectName and interstingly another folder with the same inside of it. Its a common behaviour of django.
  
- **Run Django Project** : To run django project first we can go to the project directory and run the manage.py file with runserver. The command is : ```python manage.py runserver``` . If we want to specify the port we can add it after runserver.
  
- **How Django works** : When a user interect with django page through browser, first user send a request for a website and then this request is forwarded to Django framework and then the request is send to url resolver and url resolver resolve the user request url and then send the request to its respactive urls.py file where all urls are listed and there is a posibility send that request further respactive urls.py file to get the disire Views.py where all logic and functionaliy is maintained to process the request, if nessecery then interect with database with help of models if not neccessary it execute a response and then send back to django framework to show the result or response to the user and also we use tamplates to send the response to the django framework. The below image illustrate it more
  
  ![DjangoIntenels](./docs/img/django_working.png)

- **Create templates** - Creating templates in django is very important to enhence the power of django. For creating it first create a folder named as "templates" and inside it create a html file named as index or anything and then in the views.py we need to import "render" from "django.shortcuts" and then return render with help of request and path of the html file ("index.html") store in "templates" as parameters. And to understand this templates by django we can modify the settings.py, where there is an array of "TEMPLATES" and inside it there is a "DIRS" array and there we need to mention the "templates"(folder name)
    To load css file from static folder first we need to link the stylesheet inside index.html useing template engine by writeing this line of code : ```<link rel="stylesheet" href="{% static 'style.css' %}">``` and also load the static with help of template engine into the top of the index.html file. code line is : ```{% load static %}```. And then go to settings.py to setup the "STATICFILES_DIRS" as [os.path.join(BASE_DIR, 'static')]. the complete code line is ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]``` to work os we need to import os in settings.py 