import logging
import os
import time

import psycopg
from flask import Flask, jsonify, render_template

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


class DatabaseConnectionError(Exception):
    """Raised when PostgreSQL cannot be reached."""


# The database connection is created when the application starts.
# Keeping it as None during import allows pytest to import app.py
# without requiring PostgreSQL to be running.
conn = None


def connect_to_database():
    """
    Connect to PostgreSQL with retry logic.

    PostgreSQL may take a few seconds to become available when the
    application and database containers start together.
    """

    global conn

    for attempt in range(10):
        try:
            conn = psycopg.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )

            logger.info("Connected to PostgreSQL!")
            return

        except psycopg.Error:
            logger.warning(
                f"Database not ready... retrying ({attempt + 1}/10)"
            )
            time.sleep(2)

    raise DatabaseConnectionError(
        "Could not connect to PostgreSQL after 10 attempts."
    )


@app.route("/")
def home():
    """Display the employee list as an HTML page."""

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, department, email
        FROM employees
        ORDER BY id
    """)

    rows = cursor.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "email": row[3]
        })

    cursor.close()

    return render_template(
        "index.html",
        employees=employees
    )


@app.route("/employees", methods=["GET"])
def get_employees():
    """Return employees as JSON."""

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, department, email
        FROM employees
        ORDER BY id
    """)

    rows = cursor.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "email": row[3]
        })

    cursor.close()

    return jsonify(employees)


@app.route("/health")
def health():
    """
    Check whether the application can communicate with PostgreSQL.

    Docker, Kubernetes, load balancers, and monitoring systems
    can use this endpoint.
    """

    try:
        cursor = conn.cursor()

        # A simple query confirms that PostgreSQL is responding.
        cursor.execute("SELECT 1")

        cursor.close()

        logger.info("Health check passed")

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except psycopg.Error as e:
        logger.error(f"Health check failed: {e}")

        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }), 500


# This runs only when we execute: python app.py
# pytest can import the application without starting it.
if __name__ == "__main__":
    connect_to_database()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
