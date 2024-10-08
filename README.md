# 🛒 E-commerce-Backend

This is the backend of an e-commerce web application, built using **Django**. It provides robust functionalities to handle the server-side logic of an e-commerce platform, including user authentication, product management, shopping cart, order processing, and more.

## 📄 Key Features

- **User Management**: Registration, login, and profile management.
- **Product Management**: Create, update, and delete products.
- **Shopping Cart**: Add, update, and remove products in the cart.
- **Order Processing**: Secure order placement and checkout process.
- **Blog**: Manage blog posts and updates.
- **Contact Form**: Receive customer inquiries.
- **Admin Dashboard**: Fully functional Django admin panel for managing products, orders, users, etc.

## 🚀 Technologies Used

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework (DRF)** for API endpoints
- **PostgreSQL/MySQL** for database
- **Celery** for handling asynchronous tasks (e.g., emails, background jobs)
- **Redis** for caching and queue management
- **Gunicorn** and **Nginx** for deployment

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

# create migrations
python manage.py makemigrations

# add migrations 
python manage.py migrate

# runing server
python manage.py runserver
```