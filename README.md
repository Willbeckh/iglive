# Photol

A simple Instagram clone built with love and Django.

# Prerequisites

To install this project in your machine, Install the following packages:

- Python3
- Virtualenv
- PostgreSQL
- VsCode

# Technology

- Python3
- Django 4.0
- Bootsrap 4
- Javascript
- HTML
- CSS

# Tooling

1. Virtualenv
2. PostgreSQL
3. Heroku
4. VsCode

# Installing

Create a virtual environment and install the required packages.

```bash
# Create a virtual environment
python3 - m venv venv
# activate env
source venv/bin/activate
# install packages
pip install - r requirements.txt
```

Inside the project directory, create a dotenv file.

```bash
touch .env
```

Add the follwing credentials to the .env file:

```bash
DB_USER = <username >
DB_PASSWORD = <password >
DB_HOST = <host >
DB_PORT = <port >
DB_NAME = <dbname >
SECRET_KEY = <secret_key >
MODE = 'dev'

CLOUDINARY_CLOUD_NAME = <cloud_name >
CLOUDINARY_API_KEY = <api_key >
CLOUDINARY_API_SECRET = <api_secret >

```

# Running

To run the application, run the following command:

```bash
python3 manage.py runserver
```

# Database

First, create a database of your choice and save the credentials in `.env`.:

to Get the database up and running run:

```bash
python3 manage.py migrate
```

# Testing

This application is created followint the TDD model for database models and their methods respectibvely.
To run the tests use:

```bash
python3 manage.py test
```

# Deploying

To deploy the application to Heroku follow this guide: [Heroku deploy](https: // gist.github.com/bernie-haxx/01e28cfbd911f87c7df8ee33cbdaa593)

Aslo click here to see a version of this project deployed to Heroku: [Picasso Gallery](https://photol.herokuapp.com/)

# Contributing

Feel free to fork and tweak as you like:)
or you can also open an issue or PR: [here](https://github.com/Willbeckh/iglive/pulls)

# Known Issues

At the moment of completion and deploy, no bigs have been found yet, but if you find any you know what it is, it's a feature : )

# Author

Created with ❤️ by Willbeckh.

# Credits
Me, and StackOverflow.

# License

This project is licensed under the[MIT license](LICENSE).
