# E-commerse-backend

### Runing project

```bash
# cloning repositoriy
git clone https://github.com/RustamovAkrom/E-commerse-backend.git

# go over to E-commerse-backend dir
cd E-commerse-backend

# install dependencias
pip install -r requirements.txt

# create and configure .env fayil in working direktoriy
# example arguments fayil: .env-example

# add migrations 
python manage.py migrate

# runing server
python manage.py runserver
```

## Texnologies

List the technologies and libraries used:

- Python
- Django
- PostgreSQL

## Project structure

```bash
/E-commerse-backend
    /apps
        /shared
            /migrations
                /__init__.py
            /__init__.py
            /admin.py
            /apps.py
            /models.py
            /test.py
            /views.py
    /core
        /config
            /__init__.py
            /apps.py
        /__init__.py
        /asgi.py
        /settings.py
        /urls.py
        /wsgi.py
    /static
        /...
    /media
        /...
    .env
    requirements.txt
    manage.py
    README.md

```
