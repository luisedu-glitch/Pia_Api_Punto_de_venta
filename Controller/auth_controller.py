
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from DB.db import Database

auth_bp = Blueprint("auth", __name__)
db = Database()

@auth_bp.post("/login")
def login():

    data = request.get_json(force=True)
    username = data.get("Correo")
    password = data.get("contrasena")

    if not username or not password:
        return jsonify({"error": "Usuario y contraseña requeridos"}), 400

    conn = db.connect()
    cur = conn.cursor(buffered=True)

    try:
        cur.execute(
            "CALL sp_login(%s, %s)",
            (username, password)
        )

        row = cur.fetchone()

        while cur.nextset():
            pass

        cur.close()
        conn.close()

        if not row:
            return jsonify(error="Usuario o contraseña incorrecta"), 401

        # Generar token
        access_token = create_access_token(identity=str(row[0]))

        return jsonify(access_token=access_token)

    except Exception as e:
        print("Error en login:", e)
        return jsonify(error="Error en el servidor"), 500


