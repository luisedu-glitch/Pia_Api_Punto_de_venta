from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services import venta_service

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services import venta_service


venta_bp = Blueprint("venta_bp", __name__)


@venta_bp.route('/ventas', methods=['POST'])
@jwt_required()
def registrar_venta():
    datos = request.get_json(silent=True)

    # CAMBIO: se llama a la clase VentaService
    res, msg, status_code = venta_service.VentaService.realizar_venta(datos)

    if res is None:
        return jsonify({
            "status": "error",
            "message": msg,
            "data": None
        }), status_code

    return jsonify({
        "status": "success",
        "message": msg,
        "data": res
    }), status_code