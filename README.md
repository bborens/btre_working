#Create Django R\E web app 
create python virutal environment.
kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python3 -m venv ./venv

activate virtual environment
kde-bot@kde-bot-MS-7751:~/dev/btre_app$ source ./venv/bin/activate

Now from within the virtual environment...
pgrade Pip as needed
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ pip install --upgrade pip
Install Django
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ pip install django
reate project 
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ django-admin startproject btre .
Upgrade pylint
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ /home/kde-bot/dev/btre_app/venv/bin/python -m pip install -U pylint

Run python server on loopback : access : localhost:8000
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py runserver

Create pages app & add app name to btre/settings.py
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py startapp pages

Go to settings.py add
 'DIRS': [os.path.join(BASE_DIR, 'templates')],

 Create templates folder in root. link urls.py to views.py
 Create static files with css static images. 
 update .gitignore with /static
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py collectstatic

Format Partials folder within templates
_topbar
_navbar
_footer

(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py startapp listings
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py startapp realtors
Realtors is for model, creating through admin area + relationship to listning with Postgres

POSTGRES SCHEMAS

from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

from django.db import models 
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=2)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField() 
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

    Create Migrations file
    (venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py makemigrations
    Migrations for 'realtors':
    realtors/migrations/0001_initial.py
    - Create model Realtor
    Migrations for 'listings':
    listings/migrations/0001_initial.py
    - Create model Listing

    Create Superuser for admin area
    (venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python manage.py createsuperuser

    CREATE REALTORS / LISTINGS form in Django Admin by admin.py files and importing models. 
            
    # Add data and Media Folder. 
            > Models will create simple forms in Django Admininstration 
            > Check pgAdmin 4 connections. 
        
    # Style Admin Page with theme
            > update backend themeing. 
            > create /admin folder within /templates
            > cd /admin
            > touch && nano base_site.html (Changes 'Django Admin' > Company Branding by extending blocks)
                $ {% extends 'admin/base.html' %}
                    {% load static %}

                    {% block branding %}
                        <h1 id="head">
                            BT Real Estate
                        </h1>
                    {% endblock %}

    # Customizing Admin Display Data
                    
                $   class RealtorAdmin(admin.ModelAdmin):
                    list_display = ('id', 'name', 'email', 'hire_date')
                    list_display_links = ('id', 'name')
                    search_fields = ('name',)
                    lists_per_page = 25

                $   class ListingAdmin(admin.ModelAdmin):
                    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
                    list_display_links = ('id', 'title')
                    list_filter = ('realtor',)
                    list_editable = ('is_published',)
                    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
                    list_per_page = 25

