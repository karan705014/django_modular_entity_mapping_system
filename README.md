# Django Modular Entity Mapping System

A Django REST Framework project that demonstrates a **modular backend architecture** where multiple master entities are managed independently and their relationships are maintained using mapping tables.

The system provides REST APIs for managing Vendors, Products, Courses, and Certifications, along with APIs to maintain relationships between them.

---

# Project Overview

This project is designed to show how **modular architecture and relational data modeling** can be implemented in Django using REST APIs.

The system contains four main entities:

* Vendor
* Product
* Course
* Certification

These entities are connected using mapping tables to maintain relationships.

---

# Entity Relationship Flow

Vendor → Product → Course → Certification

Example:

Vendor (TCS)
→ Product (Laptop)
→ Course (Python Course)
→ Certification (Python Certification)

---

# Project Structure

```
project_root
│
├── vendor
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── product
│
├── course
│
├── certification
│
├── vendor_product_mapping
│
├── product_course_mapping
│
├── course_certification_mapping
│
└── project_settings
```

Each module is independent and handles its own functionality.

---

# Features

* Modular Django Architecture
* REST APIs using Django REST Framework
* CRUD operations for all entities
* Mapping APIs to maintain relationships
* API documentation using Swagger (drf-yasg)
* Clean and scalable project structure

---

# Entities

## Vendor

Stores vendor information.

Example:

```
{
"name": "TCS",
"code": "V001",
"description": "IT Vendor",
"is_active": true
}
```

---

## Product

Stores product details.

Example:

```
{
"name": "Laptop",
"code": "P001",
"description": "Dell Laptop",
"is_active": true
}
```

---

## Course

Stores course information.

Example:

```
{
"name": "Python Django",
"code": "C001",
"description": "Backend development course",
"is_active": true
}
```

---

## Certification

Stores certification details.

Example:

```
{
"name": "AWS Certification",
"code": "CERT001",
"description": "Cloud certification",
"is_active": true
}
```

---

# Mapping APIs

Mapping tables maintain relationships between entities.

## Vendor Product Mapping

Example request:

```
POST /vendor-product-mapping/

{
"vendor": 1,
"product": 1
}
```

Meaning:

Vendor 1 sells Product 1.

---

## Product Course Mapping

```
POST /product-course-mapping/

{
"product": 1,
"course": 1
}
```

Meaning:

Product 1 is associated with Course 1.

---

## Course Certification Mapping

```
POST /course-certification-mapping/

{
"course": 1,
"certification": 1
}
```

Meaning:

Course 1 provides Certification 1.

---

# API Documentation

Swagger documentation is available at:

```
http://127.0.0.1:8000/swagger/
```

This allows easy testing of all APIs directly from the browser.

---

# Technologies Used

* Python
* Django
* Django REST Framework
* Swagger (drf-yasg)
* SQLite

---

# How to Run the Project

Clone the repository:

```
git clone https://github.com/yourusername/django-modular-entity-mapping-system.git
```

Navigate to project folder:

```
cd django-modular-entity-mapping-system
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Run server:

```
python manage.py runserver
```

---

# Learning Objectives

This project demonstrates:

* Modular backend architecture
* REST API development
* Entity relationship management
* Django app modularization
* API documentation using Swagger

---

# Author

Karan Singh
