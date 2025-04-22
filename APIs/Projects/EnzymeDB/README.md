# Enzyme DB

![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django) ![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
## Overview
EnzymeDB is a RESTful API service built with Django REST Framework that provides a comprehensive database of enzymes. The API allows users to create, read, update, and delete enzyme entries with proper authentication and authorization.


## Features

- RESTful API endpoints for enzyme data management
- User authentication and authorization
- Token-based authentication
- API documentation with Swagger/OpenAPI
- Browsable API interface
- User registration and login functionality
- Role-based access control (Regular users and Superusers)

## Technology Stack

- Python 3.12
- Django 5.2
- Django REST Framework 3.16.0
- drf-yasg 1.21.10 (API documentation)
- django-allauth (Authentication)
- dj-rest-auth (REST API authentication)
- SQLite (Database)

## 📂 Project Organization

```
EnzymeDB/
│
├── enzyme_api/ # Main application directory
│ ├── migrations/ # Database migrations
│ ├── init.py
│ ├── admin.py # Admin interface configuration
│ ├── apps.py # App configuration
│ ├── auth.py # Custom authentication views
│ ├── models.py # Database models
│ ├── permissions.py # Custom permission classes
│ ├── serializers.py # API serializers
│ ├── urls.py # API URL routing
│ └── views.py # API views
│
├── enzyme_db/ # Project configuration directory
│ ├── init.py
│ ├── asgi.py # ASGI configuration
│ ├── settings.py # Project settings
│ ├── urls.py # Main URL routing
│ └── wsgi.py # WSGI configuration
│
├── .enzyme/ # Virtual environment (not tracked in git)
├── .gitignore # Git ignore file
├── README.md # Project documentation
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
└── requirements.txt # Project dependencies
```
## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd EnzymeDB
```

2. Create and activate a virtual environment:
```bash
python -m venv .enzyme
source .enzyme/bin/activate  # On Windows, use `.enzyme\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints

- `POST /auth/register/` - Register a new user
- `POST /auth/login/` - Login user
- `POST /api/v1/rest-auth/login/` - Login (dj-rest-auth)
- `POST /api/v1/rest-auth/logout/` - Logout (dj-rest-auth)
- `POST /api/v1/rest-auth/registration/` - Register (dj-rest-auth)
- `GET /api-auth/login/` - Browsable API login

### API Documentation

- `/swagger/` - Swagger UI documentation
- `/redoc/` - ReDoc documentation
- `/swagger.json` - OpenAPI specification in JSON

### Main API Endpoints

- `GET /api/v1/enzymes/` - List all enzymes (filtered by user permissions)
- `POST /api/v1/enzymes/` - Create a new enzyme
- `GET /api/v1/enzymes/{id}/` - Retrieve a specific enzyme
- `PUT /api/v1/enzymes/{id}/` - Update a specific enzyme
- `DELETE /api/v1/enzymes/{id}/` - Delete a specific enzyme

## Authentication

The API uses token-based authentication. To access protected endpoints:

1. Register a new user or login with existing credentials
2. Include the token in the Authorization header:


## Permissions

- **Superusers** have full access to all endpoints and can view/modify all enzyme entries
- **Regular users** can:
  - View their own enzyme entries
  - Create new enzyme entries
  - Modify their own entries
  - Cannot modify other users' entries

## Development

To format code using Black:
```bash
black .
```

## API Documentation

The API documentation is available through:

1. Swagger UI: Visit `/swagger/` for interactive documentation
2. ReDoc: Visit `/redoc/` for a more readable documentation format

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the **MIT License**.

## 📧 Contact

[Joshua Yentumi](ampofojoshauyent@gmail.com)
