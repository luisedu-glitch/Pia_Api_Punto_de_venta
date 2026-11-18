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
        return jsonify({"error":"Usuario y contraseña requeridos"}), 400

    # Verificar usuario en BD
    conn = db.connect()
    cur = conn.cursor()
    cur.execute("SELECT contrasena FROM usuario WHERE Correo=%s", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return jsonify(error="Usuario no encontrado"), 401

    stored_password = row[0]

    if stored_password != password:
        return jsonify(error="Contraseña incorrecta"), 401

    # Generar token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)