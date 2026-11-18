from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services import usuario_service

usuario_bp = Blueprint("usuario_bp", __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def listar_usuarios():
    usuarios = usuario_service.obtener_todos()
    return jsonify({"status": "success", "message": "Operación realizada correctamente", "data": usuarios}), 200

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
@jwt_required()
def obtener_usuario(id_usuario):
    usuario = usuario_service.obtener_por_id(id_usuario)
    if not usuario:
        return jsonify({"status": "error", "message": "Usuario no encontrado", "data": None}), 404
    return jsonify({"status": "success", "message": "Operación realizada correctamente", "data": usuario}), 200

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
@jwt_required()
def actualizar_usuario(id_usuario):
    datos = request.get_json()
    exito = usuario_service.actualizar_usuario(id_usuario, datos)
    if not exito:
        return jsonify({"status": "error", "message": "Usuario no encontrado o sin cambios", "data": None}), 404
    return jsonify({"status": "success", "message": "Usuario actualizado correctamente", "data": None}), 200