from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "customers.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
    """)

    connection.commit()
    connection.close()


@app.route("/customers", methods=["POST"])
def create_customer():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name:
        return jsonify({
            "error": "Name is required"
        }), 400

    if not email:
        return jsonify({
            "error": "Email is required"
        }), 400

    connection = get_db_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO customers (name, email, phone)
            VALUES (?, ?, ?)
            """,
            (name, email, phone)
        )

        connection.commit()

        customer_id = cursor.lastrowid

        return jsonify({
            "message": "Customer created successfully",
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone": phone
        }), 201

    except sqlite3.IntegrityError:

        return jsonify({
            "error": "Email already exists"
        }), 409

    finally:
        connection.close()


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):

    connection = get_db_connection()

    customer = connection.execute(
        "SELECT * FROM customers WHERE id = ?",
        (customer_id,)
    ).fetchone()

    connection.close()

    if customer is None:
        return jsonify({
            "error": "Customer not found"
        }), 404

    return jsonify(dict(customer)), 200


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    connection = get_db_connection()

    existing_customer = connection.execute(
        "SELECT * FROM customers WHERE id = ?",
        (customer_id,)
    ).fetchone()

    if existing_customer is None:
        connection.close()

        return jsonify({
            "error": "Customer not found"
        }), 404

    try:

        connection.execute(
            """
            UPDATE customers
            SET name = ?, email = ?, phone = ?
            WHERE id = ?
            """,
            (name, email, phone, customer_id)
        )

        connection.commit()

        return jsonify({
            "message": "Customer updated successfully",
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone": phone
        }), 200

    except sqlite3.IntegrityError:

        return jsonify({
            "error": "Email already exists"
        }), 409

    finally:
        connection.close()


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):

    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM customers WHERE id = ?",
        (customer_id,)
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    if deleted == 0:
        return jsonify({
            "error": "Customer not found"
        }), 404

    return jsonify({
        "message": "Customer deleted successfully"
    }), 200


if __name__ == "__main__":
    initialize_database()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )