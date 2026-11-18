
from flask import Blueprint, jsonify
from services.reporte_service import reporteservice

reporte_bp = Blueprint("reportes", __name__)


# =========================================
# REPORTE DE VENTAS POR CAJA
# =========================================

@reporte_bp.get("/reportes/ventas-por-caja")
def ventas_por_caja():

    try:
        reportes = reporteservice.listar_ventas_por_caja()

        resultado = [
            r.a_diccionario() for r in reportes
        ]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({
            "error": "Error al obtener ventas por caja",
            "detalle": str(e)
        }), 500


# =========================================
# REPORTE DE VENTAS POR PRODUCTO
# =========================================

@reporte_bp.get("/reportes/ventas-por-producto")
def ventas_por_producto():

    try:
        reportes = reporteservice.listar_ventas_por_producto()

        resultado = [
            r.a_diccionario() for r in reportes
        ]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({
            "error": "Error al obtener ventas por producto",
            "detalle": str(e)
        }), 500


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
