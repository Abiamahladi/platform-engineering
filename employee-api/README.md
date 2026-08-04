# Employee Management System

## Overview

The Employee Management System is a containerized web application built with **Flask**, **PostgreSQL**, and **Docker Compose**.

The project demonstrates how a web application communicates with a database inside Docker using service discovery, environment variables, Docker volumes, and persistent storage.

This project is part of my **Platform Engineering** portfolio and focuses on building a production-style application from the ground up.

---

# Objectives

The goals of this project are to:

* Build a Flask web application.
* Store employee records in PostgreSQL.
* Containerize the application using Docker.
* Orchestrate multiple containers with Docker Compose.
* Learn Docker networking and service discovery.
* Persist database data using Docker volumes.
* Initialize the database automatically using SQL scripts.

---

# Technologies Used

* Python 3.13
* Flask
* PostgreSQL 17
* Docker
* Docker Compose
* HTML
* Jinja2 Templates
* SQL

---

# Architecture

```text
                Browser
                    │
                    ▼
         http://localhost:5000
                    │
                    ▼
          Flask Application
                    │
       Docker Service Discovery
                    │
                    ▼
          PostgreSQL Database
                    │
                    ▼
             Docker Volume
```

---

# Project Structure

```text
employee-api/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── db/
│   └── init.sql
│
└── templates/
    └── index.html
```

---

# Features

Current features include:

* Register a new employee
* View all employees
* Store employee records in PostgreSQL
* Automatic database initialization
* Persistent database storage using Docker volumes
* Containerized application
* Docker Compose orchestration

---

# Running the Application

## Build and start

```bash
docker compose up --build
```

## Open the application

```
http://localhost:5000
```

## Stop the application

```bash
docker compose down
```

## Remove containers and database volume

```bash
docker compose down -v
```

---

# API Endpoints

## Home Page

```
GET /
```

Displays the Employee Registration page.

---

## Get Employees

```
GET /employees
```

Returns all employees as JSON.

---

## Add Employee

```
POST /employees
```

Creates a new employee record in PostgreSQL.

---

# Database Initialization

The database is automatically initialized using:

```text
db/init.sql
```

During the first startup Docker automatically:

* Creates the employees table.
* Inserts sample employee records.

---

# Lessons Learned

This project helped me gain practical experience with:

* Docker Images
* Docker Containers
* Docker Compose
* Docker Networking
* Docker Volumes
* Bind Mounts
* Service Discovery
* Environment Variables
* Flask
* PostgreSQL
* HTML Forms
* Database Initialization
* Container Debugging

---

# Future Improvements

Planned enhancements include:

* Edit employee
* Delete employee
* Search employee
* Bootstrap user interface
* Nginx reverse proxy
* Kubernetes deployment
* GitHub Actions CI/CD pipeline

---

# Author

**Abiamahladi Nkweke**

DevOps & Platform Engineering Portfolio

This project is part of my hands-on learning journey in Cloud, DevOps, and Platform Engineering.

