# UdaCredit Union App

## Overview
This is a lightweight application built with ReactJS for the frontend and Flask for the backend API. It's built as a slimmed-down application intended to represent a simple monolith application. API responses are static so that we don't need to set up a database to keep the complexity low.

## Instructions
You should have Docker installed on your machine.
```
docker-compose up --build
```
The command should take a few minutes to run. This will create multiple Docker containers as specified in the `docker-compose.yml` file.

For subsequent runs, you can run `docker-compose up` without the `--build` command.

* The Flask application can be found at `http://localhost:5000`:
    `http://localhost:5000/api/employees`

    `http://localhost:5000/api/customers`

* The UI can be found at `http://localhost:3000`

The application can be killed by holding `CTRL+C` or cleanly shut down with `docker-compose down`.
