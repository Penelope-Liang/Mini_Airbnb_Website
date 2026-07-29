# StayNest

StayNest is a small vacation-rental web application built with Flask. It supports account registration, login, profile updates, listing creation, listing updates, bookings, and booking history.

This repository is maintained as a personal project version of a vacation-rental marketplace app.

## Features

- User registration and login
- Profile editing
- Property listing creation and updates
- Booking flow
- My bookings view
- Input validation and security tests
- Docker Compose setup with MySQL and phpMyAdmin

## Tech Stack

- Python
- Flask
- SQLite for local development
- MySQL through Docker Compose
- HTML and CSS templates
- Pytest, SeleniumBase, and Flake8 for testing

## Project Structure

```text
qbay/               Application code and templates
qbay_test/          Backend, frontend, and security tests
db_init.sql         Database initialization script
docker-compose.yml  Docker services for the app and database
Dockerfile          App container image definition
pkg.txt             Python dependencies
```

## Run Locally

Install dependencies:

```bash
pip install -r pkg.txt
```

Start the Flask app:

```bash
python3 -m qbay
```

The app runs on:

```text
http://localhost:8080
```

## Run With Docker

```bash
docker compose up --build
```

App:

```text
http://localhost:8080
```

phpMyAdmin:

```text
http://localhost:8082
```

## Tests

Run the test suite:

```bash
python3 -m pytest
```

Run style checks:

```bash
flake8 qbay qbay_test
```

## License

This project keeps the original MIT license notice included in `LICENSE`.
