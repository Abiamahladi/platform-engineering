from flask import Flask, jsonify, request, render_template, redirect, url_for
import psycopg
import os
import time

app = Flask(__name__)

# Wait for PostgreSQL to become available
conn = None

for attempt in range(10):
    try:
        conn = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("✅ Connected to PostgreSQL!")
        break

    except Exception:
        print(f"Database not ready... retrying ({attempt + 1}/10)")
        time.sleep(2)

if conn is None:
    raise Exception("Could not connect to PostgreSQL after 10 attempts.")


@app.route("/")
def home():

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


@app.route("/employees", methods=["POST"])
def add_employee():

    name = request.form["name"]
    department = request.form["department"]
    email = request.form["email"]

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO employees (name, department, email)
        VALUES (%s, %s, %s)
        """,
        (name, department, email)
    )

    conn.commit()

    cursor.close()

    return redirect(url_for("home"))

@app.route("/health")
def health():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
