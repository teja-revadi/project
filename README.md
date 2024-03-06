# Simple Notes App

This is a simple Django app for managing notes, integrated with Swagger for API documentation.
It has sample test cases in test.py to test the backend code.
It also has a frontend UI to see,search and create notes.

## Features

- Create, read, update notes.
- Swagger integration for easy API documentation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/teja-revadi/simple-notes-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd simple-notes-app
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    \venv\Scripts\activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the app in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Testing
To test the sample test cases:

 ```bash
 python manage.py test.py
 ```

## API Documentation

You can access the Swagger documentation for the API at [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/).

## Usage

Visit [http://127.0.0.1:8000/api/home](http://127.0.0.1:8000/api/home) to view and manage your notes in frontend.
Use the Swagger documentation to explore and interact with the API endpoints.
