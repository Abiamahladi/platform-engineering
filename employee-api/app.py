
import logging
import os

import psycopg
from flask import Flask, jsonify, render_template

# =========================================================
# LOGGING
# =========================================================
# In Kubernetes, application logs are normally viewed with:
#
#     kubectl logs <pod>
#
# We therefore send our application logs to stdout/stderr.
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# DATABASE CONNECTION
# =========================================================
# We do NOT keep a global database connection.
#
# Every request that needs PostgreSQL gets a connection,
# uses it, and then closes it.
#
# The database credentials come from environment variables:
#
#     DB_NAME
#     DB_USER
#     DB_PASSWORD
#     DB_HOST
#     DB_PORT
#
# Kubernetes provides these environment variables to the
# Employee API Pod. The password ultimately comes from Vault.
# =========================================================

def get_db_connection():
    """Create and return a PostgreSQL connection."""

    try:
        connection = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        logger.info("Connected to PostgreSQL")

        return connection

    except psycopg.Error as e:
        logger.error(f"Database connection failed: {e}")

        raise


# =========================================================
# HOME PAGE
# =========================================================
# GET /
#
# Displays the employees as an HTML page.
# =========================================================

@app.route("/")
def home():
    """Display the employee list as an HTML page."""

    db = get_db_connection()

    try:
        cursor = db.cursor()

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

    finally:
        # Always close the database connection.
        #
        # This runs even if the SQL query fails.
        db.close()


# =========================================================
# EMPLOYEE API
# =========================================================
# GET /employees
#
# Returns employees as JSON.
# =========================================================

@app.route("/employees", methods=["GET"])
def get_employees():
    """Return employees as JSON."""

    db = get_db_connection()

    try:
        cursor = db.cursor()

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

    finally:
        # Close the database connection when finished.
        db.close()


# =========================================================
# HEALTH CHECK
# =========================================================
# GET /health
#
# This endpoint checks both:
#
#     1. Is the application running?
#     2. Can the application connect to PostgreSQL?
#
# Kubernetes can later use this endpoint for health probes.
# =========================================================

@app.route("/health")
def health():
    """Check whether the application can communicate with PostgreSQL."""

    db = None

    try:
        db = get_db_connection()

        cursor = db.cursor()

        # SELECT 1 is a simple query used to confirm that
        # PostgreSQL is accepting queries.
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
            "database": "disconnected"
        }), 500

    finally:
        # If a connection was successfully created,
        # close it before finishing the request.
        if db is not None:
            db.close()


# =========================================================
# LOCAL DEVELOPMENT
# =========================================================
# This section is only used when running:
#
#     python app.py
#
# Our Kubernetes Deployment uses Gunicorn instead.
#
# Gunicorn imports "app" directly, so it does NOT depend
# on this section to initialize the application.
# =========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
