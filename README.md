# Employee Management REST API

A simple and clean **Employee Management REST API** built using **Django Rest Framework** as part of the **HabotConnect hiring assignment**. This project demonstrates backend fundamentals such as authentication, CRUD APIs, filtering, pagination, and clean project structure.

---

## Project Overview

This API allows an organization to manage employee records securely. All employee-related operations are protected using **JWT authentication**. The project is designed following RESTful best practices and focuses on clarity, readability, and maintainability.

## Key Features

- JWT-based authentication (Login & Token Refresh)
- Create, Read, Update, Delete (CRUD) Employees
- Email uniqueness & validation
- Search employees by name or email
- Filter employees by department and role
- Pagination support (default: 10 records per page)
- Proper HTTP status codes & error handling
- Django Admin support

---

##  Tech Stack

- **Python** 3.8+
- **Django** 
- **Django REST Framework**
- **Simple JWT** for authentication
- **SQLite** (development database)

---

## Project Structure

```
employee_api/
│── employee_api/        # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── employees/           # Employee app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
│── manage.py
│── db.sqlite3
│── requirements.txt
│── README.md
```

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DrashtiDholariya/employee_api.git
cd employee_api
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv evenv
source evenv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

[Server will run ](http://127.0.0.1:8000/)at: [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/)

---

## Authentication (JWT)

### Obtain Token

**POST** `/api/token/`

```json
{
  "username": "admin",
  "password": "your_password"
}
```

Use the **access token** in headers:

```
Authorization: Bearer <access_token>
```

### Refresh Token

**POST** `/api/token/refresh/`

---

## Employee API Endpoints

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| POST   | `/api/employees/`      | Create employee   |
| GET    | `/api/employees/`      | List employees    |
| GET    | `/api/employees/{id}/` | Retrieve employee |
| PUT    | `/api/employees/{id}/` | Update employee   |
| DELETE | `/api/employees/{id}/` | Delete employee   |

---

## Filtering & Search

- Filter by department:

```
/api/employees/?department=Engineering
```

- Filter by role:

```
/api/employees/?role=Developer
```

- Search:

```
/api/employees/?search=john
```

---

## Pagination

- Default page size: **10**
- Example:

```
/api/employees/?page=2
```

---

## Testing

Run tests using:

```bash
python manage.py test
```

---

## Admin Panel

Access Django Admin at:

```
http://127.0.0.1:8000/admin/
```

---

## Developer Details

- **Name:** Drashti Dholariya
- **Role Applied:** Python Backend Developer
- **Project For:** HabotConnect Hiring Process

---

## Final Note

This project focuses on clean backend architecture, proper authentication, and real-world API practices. It is structured to be easily extendable and production-ready.

Thank you for reviewing this project!

