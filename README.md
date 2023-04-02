# Django-e-commerce - Secure

## Run application locally

To start, we want to make sure we're in the correct directory.
You should cd into where manage.py is located, which is `.../Django-e-commerce/e_commerce/`

The project has a few dependencies so to run it locally, you can either create a virtualenv
or install the packages yourself, for this setup on how to run the application, we will be using virtualenv.

``
pip install --user virtualenv
``

``
virtualenv env
``

if you ls in the terminal, you should see a new folder with the new env folder located.
From there, we will run 

``
./env/Scripts/activate
``

Now you should be in the virtual env. From there, we will install our dependencies

- We will first type `pip install Django` into the terminal to install Django
- We will then type `pip install django-bootstrap3` into the terminal to install bootstrap
- Again, we will type `pip install Pillow` into the terminal to install Pillow

With all of our dependencies installed, we can start the application. 
First, you will want to check that you are still in the same directory as the manage.py file. If not, cd into it. 

Once you're in the right directory, type `python manage.py runserver` into the terminal to start the application.
Depending on versioning, this may be `py manage.py runserver` so check if your environment variables if this doesn't work.

With that, the server should start and display the following

```yaml
Django version 4.1.7, using settings 'e_commerce.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Your development server may differ so click whatever link comes up, in my case, I will be clicking or copy and pasting 
http://127.0.0.1:8000/ into the web browser

At this point you should now see the web application and are able to explore the settings there. 

FYI: use http://127.0.0.1:8000/admin/ for an admin view of the app