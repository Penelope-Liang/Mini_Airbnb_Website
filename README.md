# Mini Airbnb Website

Mini Airbnb Website is a small vacation-rental web application built with Flask. It provides a simple marketplace where users can register, log in, manage their profile, create property listings, update listings, book accommodations, and view booking history.

## Features

- User registration and login
- Profile editing
- Property listing creation and update
- Accommodation booking workflow
- Booking history page
- Input validation and security test coverage
- Docker Compose setup with MySQL and phpMyAdmin

## Tech Stack

- Python
- Flask
- SQLite for local development
- MySQL through Docker Compose
- HTML/CSS templates
- Pytest, SeleniumBase, and Flake8 for testing

## Requirements

- Python 3.7+
- pip
- Docker and Docker Compose, if running the containerized setup

## Project Structure

```text
qbay/               Application code and templates
qbay_test/          Backend, frontend, and security tests
.github/workflows/  GitHub Actions test, style, and CD workflows
db_init.sql         Database initialization script
docker-compose.yml  Docker services for the app and database
Dockerfile          App container image definition
pkg.txt             Python dependencies
wait-for-it.sh      Helper script used by Docker Compose to wait for MySQL
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

Local runs use SQLite by default through `data.db`.

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

The Docker Compose setup runs the Flask app with MySQL through the `db_string`
environment variable.

## Testing

Run the test suite:

```bash
python3 -m pytest qbay_test
```

Run style checks:

```bash
flake8 --select=E .
```

## CI/CD

GitHub Actions runs automated tests and style checks on pushes and pull
requests. The CD workflow publishes the Docker image to GitHub Container
Registry when changes are pushed to `main`, when a `v*` tag is pushed, or when
the workflow is started manually.

Published image format:

```text
ghcr.io/<owner>/<repository>:latest
```

## License

This project keeps the original MIT license notice included in `LICENSE`.
