from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services import usuario_service
import base64
usuario_bp = Blueprint("usuario_bp", __name__)



@usuario_bp.route('/usuarios', methods=['POST'])
@jwt_required()
def crear_usuario():
    if request.content_type and request.content_type.startswith("multipart/form-data"):
        datos = request.form.to_dict()
        archivo = request.files.get("imagen")
        datos["imagen"] = archivo.read() if archivo else None
    else:
        datos = request.get_json(silent=True) or {}
        img64 = datos.get("imagen")
        datos["imagen"] = base64.b64decode(img64) if img64 else None

    if not datos:
        return jsonify({"status": "error",
                        "message": "Datos requeridos",
                        "data": None}), 400

    id_creado = usuario_service.UsuarioService.crear(datos)

    return jsonify({
        "status": "success",
        "message": "Usuario creado correctamente",
        "data": {"id_usuario": id_creado}
    }), 201

@usuario_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def listar_usuarios():
    usuarios = usuario_service.UsuarioService.obtener_todos()

    return jsonify({
        "status": "success",
        "message": "Operación realizada correctamente",
        "data": usuarios
    }), 200


@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
@jwt_required()
def obtener_usuario(id_usuario):
    usuario = usuario_service.UsuarioService.obtener_por_id(id_usuario)

    if not usuario:
        return jsonify({
            "status": "error",
            "message": "Usuario no encontrado",
            "data": None
        }), 404

    return jsonify({
        "status": "success",
        "message": "Operación realizada correctamente",
        "data": usuario
    }), 200


@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
@jwt_required()
def actualizar_usuario(id_usuario):
    if request.content_type and request.content_type.startswith("multipart/form-data"):
        datos = request.form.to_dict()
        archivo = request.files.get("imagen")
        if archivo:
            datos["imagen"] = archivo.read()
    else:
        datos = request.get_json(silent=True) or {}
        img64 = datos.get("imagen")
        if img64:
            datos["imagen"] = base64.b64decode(img64)
        else:
            datos.pop("imagen", None)

    if not datos:
        return jsonify({
            "status": "error",
            "message": "No se enviaron datos para actualizar",
            "data": None
        }), 400

    # 404 real si el usuario no existe
    if not usuario_service.UsuarioService.obtener_por_id(id_usuario):
        return jsonify({
            "status": "error",
            "message": "Usuario no encontrado",
            "data": None
        }), 404

    usuario_service.UsuarioService.actualizar_usuario(id_usuario, datos)

    return jsonify({
        "status": "success",
        "message": "Usuario actualizado correctamente",
        "data": None
    }), 200
