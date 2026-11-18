
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from services.producto_service import productoservice

producto_bp = Blueprint("productos", __name__)


# =====================================================
# VALIDAR DATOS
# =====================================================

def validar_datos(descripcion, precio, existencias, unidad):

    if not descripcion or not descripcion.strip():
        return None, "La descripcion es obligatoria"

    if not unidad or not unidad.strip():
        return None, "La unidad es obligatoria"

    try:
        precio = float(precio)
        existencias = int(existencias)

        if precio <= 0:
            return None, "El precio debe ser mayor a cero"

        if existencias < 0:
            return None, "Las existencias no pueden ser negativas"

    except (ValueError, TypeError):
        return None, "Precio y existencias deben ser numericos"

    return (precio, existencias), None


# =====================================================
# CREAR PRODUCTO
# =====================================================

@producto_bp.post("/productos")
@jwt_required()
def crear_producto():

    descripcion = request.form.get("descripcion")
    precio = request.form.get("precio")
    existencias = request.form.get("existencias")
    unidad = request.form.get("unidad")

    archivo = request.files.get("imagen_de_producto")

    if descripcion is None or precio is None or existencias is None or unidad is None:
        return jsonify("Faltan campos obligatorios"), 400

    datos, error = validar_datos(
        descripcion, precio, existencias, unidad
    )

    if error:
        return jsonify(error), 400

    imagen = archivo.read() if archivo else None

    try:
        producto = productoservice.crear_producto(
            descripcion.strip(),
            datos[0],
            datos[1],
            unidad.strip(),
            imagen
        )

        return jsonify(producto.a_lista()), 201

    except Exception as e:
        return jsonify("Error al crear producto: " + str(e)), 500


# =====================================================
# LISTAR PRODUCTOS
# =====================================================

@producto_bp.get("/productos")
def listar_productos():

    try:
        productos = productoservice.listar_productos()

        resultado = [
            producto.a_lista()
            for producto in productos
        ]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify("Error al obtener productos: " + str(e)), 500


# =====================================================
# OBTENER PRODUCTO POR ID
# =====================================================

@producto_bp.get("/productos/<int:idproductos>")
def obtener_producto(idproductos):

    try:
        producto = productoservice.buscar_producto(idproductos)

        if producto is None:
            return jsonify("Producto no encontrado"), 404

        return jsonify(producto.a_lista()), 200

    except Exception as e:
        return jsonify("Error de base de datos: " + str(e)), 500


# =====================================================
# ACTUALIZAR PRODUCTO
# =====================================================

@producto_bp.put("/productos/<int:idproductos>")
@jwt_required()
def actualizar_producto(idproductos):

    descripcion = request.form.get("descripcion")
    precio = request.form.get("precio")
    existencias = request.form.get("existencias")
    unidad = request.form.get("unidad")

    archivo = request.files.get("imagen_de_producto")

    if descripcion is None or precio is None or existencias is None or unidad is None:
        return jsonify("Faltan campos obligatorios"), 400

    datos, error = validar_datos(
        descripcion, precio, existencias, unidad
    )

    if error:
        return jsonify(error), 400

    imagen = archivo.read() if archivo else None

    try:
        actualizado = productoservice.modificar_producto(
            idproductos,
            descripcion.strip(),
            datos[0],
            datos[1],
            unidad.strip(),
            imagen
        )

        if not actualizado:
            return jsonify("Producto no encontrado"), 404

        producto = productoservice.buscar_producto(idproductos)

        return jsonify(producto.a_lista()), 200

    except Exception as e:
        return jsonify("Error al actualizar producto: " + str(e)), 500


# =====================================================
# ELIMINAR PRODUCTO
# =====================================================

@producto_bp.delete("/productos/<int:idproductos>")
@jwt_required()
def eliminar_producto(idproductos):

    try:
        eliminado = productoservice.borrar_producto(idproductos)

        if not eliminado:
            return jsonify("Producto no encontrado"), 404

        return jsonify("Producto eliminado correctamente"), 200

    except Exception as e:
        return jsonify("Error al eliminar producto: " + str(e)), 500

