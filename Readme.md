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

- **Create apps in django** - We can create multiple apps inside a django project on root file. To create an app we write a command on venv as : ```python manage.py startapp <name_of_the_app>``` , after run this command a folder is created with the name which we give in name of the app and include some default file inside the folder. But in this position the project cannot aware of this newly created app so to connect with the main project we need to go to the settings.py files in root project file and add the new app in the installed app section of the settings.py file. Now if we want to use templates for this newly created app then we need to create a folder name as "templates" and inside it we need to create a folder name as the same as the newly created app name and then inside it we use html file. 
  
- **Connect with new app** - First we need to modify the views.py of the newly created app where we render the html file and the request as a parameter with help of a function. and then in the urls.py file of root project app we need to include newly created app with its urls file like ```mibits.urls``` and also give the route path. and then in the newly created app urls file add the path.

- **Jinja templates** - We can reuse the same html code into other html file useing some jinja tempates engine command. First we like to create a layout.html file where we can add all html element which are use in each and every project templates. The content or block which are dynamicaly create in app level is to be declared as a unnamed block with a block name and with help of the block name we can dynamically create the element in any app. for example:
  ``` {% block title %} Default Title {% endblock %}``` in project level templates layout file and to use it in any other app level templates as ```{% block title %} Home {% endblock %}```
  
--- 
<p style= "color: blue">Tips: 1. Its great to use django extenstion to format the django and after install press Ctrl+, and  seach for emmet and find the include language and then add a item with item: django-html and value: html. This helps to geting the suggestion in templates file</p>