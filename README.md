# Library Management System API

This is a RESTful API for managing a library of books, built with Django and Django Rest Framework. Django is a high-level Python web framework that provides a clean and pragmatic design for building web applications. It takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. Django Rest Framework is a powerful and flexible toolkit for building Web APIs, and it works seamlessly with Django.

It allows you to add, update, delete and read books from a database of books. Each book is modeled with a title, author, genre, publishing year, pages, chapters and link to read it.

The API can be accessed through HTTP requests and returns JSON responses. You can use tools like Postman or cURL to interact with the API.

# Installation

* To get started, clone this repository to your local machine:

`git clone https://github.com/Younes-ch/library-management-system.git`

`cd library-management-system`

* Create a virtual environment and install the dependencies:

`python -m venv env`

`source env/bin/activate`  # On Windows use `env\Scripts\activate`

`pip install -r requirements.txt`

# Usage

Run `python manage.py migrate`

Run `python manage.py runserver`

This will start the server on `http://localhost:8000/`. You can access the API documentation by visiting `http://localhost:8000/api/`


In addition to the API, the project includes a landing page that shows all the books in the database. The landing page also features a navbar with a search function that allows you to search for books by title, author, genre or year and you can delete & edit existing books as well. There is also an "Add" section that shows a form to add a new book to the database.

# Note

There are 2 files:
- `to_add_1.json` and `to_add_5.json`: These are 2 JSON files you can use to add books through the API with cURL or Postman, etc.. to experiment with the API.
