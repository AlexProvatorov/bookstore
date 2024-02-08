# BOOK STORE

****

## Installation
1. Clone the repository: <font color="yellow">git clone git@github.com:AlexProvatorov/bookstore.git</font>
2. Install dependencies: <font color="yellow">pip install -r requirements.txt</font>
3. Create the database: <font color="yellow">python manage.py migrate</font>
4. Create a superuser: <font color="yellow">python manage.py createsuperuser</font>
5. Run the development <font color="yellow">server: python manage.py runserver</font>

## Key Features

- User registration and authentication.
- Searching and browsing goods by various tags.
- Adding goods to the shopping cart and placing orders.
- Administrative interface for managing books, orders, and users.

## Technologies

- Django: primary framework for web application development.
- HTML/CSS/JavaScript: for creating the user interface.
- PostgreSQL: database for storing information about goods, orders, and users.

## Project Structure

- `bookstore/`: main Django application.
- `templates/`: HTML templates.
- `static/`: static files (CSS, JS, images).
- `media/`: media files uploaded by users (book covers, etc.).
- `bookstore/`: project settings.

## Contribution

If you have ideas for improving the project or found a bug, feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT](MIT_LICENSE.txt).