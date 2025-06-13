# 📚 week18-api — Simple Library Management API (Flask + SQLAlchemy)

This project is a beginner-friendly REST API built using **Flask**, **Flask-RESTful**, and **SQLAlchemy**. It manages a basic library system with support for books and authors.

---

## 🚀 Project Features

- CRUD operations for books and authors
- SQLite database via SQLAlchemy ORM (Object Relational Mapper)
- Organized folder structure (models & resources)
- Simple and clean Flask setup for learning

---

## 🧠 What is SQLAlchemy?

**SQLAlchemy** is an ORM (Object Relational Mapper) for Python that allows you to interact with the database using Python classes, instead of raw SQL queries.

### ✅ Why use it?

- Automatically converts Python objects into database rows and vice versa.
- Simplifies database operations like insert, update, delete, and query.
- Integrates perfectly with Flask.

In this project, models like `BookModel` and `AuthorModel` define the structure of the database tables using SQLAlchemy.

---

## 📁 What is `__init__.py`?

The `__init__.py` file is what turns a folder into a **Python package**. Without it:

- Python won’t recognize the folder as a module/package.
- You won’t be able to import files like: `from models.book import BookModel`

### ✅ In This Project:

- The `models/` folder contains database models, and `__init__.py` allows us to import them easily.
- The `resources/` folder contains API logic, and `__init__.py` helps in organizing them as importable modules.

Even an **empty `__init__.py` file** is useful — it just needs to exist.
