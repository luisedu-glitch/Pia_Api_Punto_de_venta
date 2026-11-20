
from flask import Blueprint, jsonify
from services.reporte_service import reporteservice

reporte_bp = Blueprint("reportes", __name__)
# =========================================
# FUNCION: TOTAL VENTAS POR CAJA
# =========================================

@reporte_bp.get("/reportes/caja/<int:numero_caja>/total")
def total_ventas_caja(numero_caja):

    try:
        total = reporteservice.total_ventas_caja(numero_caja)

        return jsonify({
            "numero_caja": numero_caja,
            "total_ventas": float(total)
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Error al calcular ventas de caja",
            "detalle": str(e)
        }), 500


# =========================================
# FUNCION: TOTAL GENERADO POR PRODUCTO
# =========================================

@reporte_bp.get("/reportes/producto/<int:idproducto>/total")
def total_producto(idproducto):

    try:
        total = reporteservice.total_generado_producto(idproducto)

        return jsonify({
            "idproductos": idproducto,
            "total_generado": float(total)
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Error al calcular total del producto",
            "detalle": str(e)
        }), 500
