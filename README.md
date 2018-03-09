# vue
Creates a base Django Project
 - App call baseapp
 - no models
 - simple IndexView in baseapp/views.py
 - simple index.html in baseapp/templates/index.html
 
 mkdir /var/www/vue
 virtualenv venv
 git clone  https://github.com/jmushtaq/vue.git .
 pip install -r requirements (installs Django 1.11)

 git config user.name "jmushtaq"
 git config user.email "jawaid_mushtaq@yahoo.com"
 git config remote.origin.url https://jmushtaq@github.com/jmushtaq/vue.git

 ./manage runserver 0.0.0.0:8000
 
 Goto http://localhost:8000/baseapp, should see "Base Django Application"
