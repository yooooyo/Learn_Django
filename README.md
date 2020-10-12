# Learn_Django
This repro is for learning Django

[Tutorial URL](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

## Pre-requirement

```bash
pip install django
```


## Create a project, a app 

- Create a django project
- Create a django app

### Create a django project

``` bash
django-admin startproject mysite
```

```bash
from the above line ,we use 'name' argument, which project name is 'mysite' :

django-admin startproject [-h] [--template TEMPLATE]
                                 [--extension EXTENSIONS] [--name FILES]
                                 [--version] [-v {0,1,2,3}]
                                 [--settings SETTINGS]
                                 [--pythonpath PYTHONPATH] [--traceback]
                                 [--no-color] [--force-color]
                                 name [directory]
positional arguments :
  name                  Name of the application or project.

```

After create project, the folder structure will be:


```bash
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### Create a django app

```bash
manage.py startapp polls
```
```bash
from above line we use 'name' arguemnt to create a app named 'polls'
```

After create app, the folder structure will be:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    polls/                        - add
        __init__.py               - add
        admin.py                  - add
        apps.py                   - add
        migrations/               - add
            __init__.py           - add
        models.py                 - add
        tests.py                  - add
        views.py                  - add
```

> Summary :
- A lots of apps can be in a project
- A lots of projects can be in a folder

```bash
rootfolder/
    project1/
        manage.py
        project1/
            ....(base stuff)
        app1/
            ....(base stuff)
        app2/
            ....(base stuff)
    
    project2/
        manage.py
        project2/
            ....(base stuff)
        app1/
            ....(base stuff)
        app2/
            ....(base stuff)
            .
            .
            .
```

