
from models.producto_model import Producto

from repositorie.producto_repository import (
    Productorepository as producto_repository
)


class productoservice:

    # ==============================================
    # CREAR PRODUCTO
    # ==============================================

    @staticmethod
    def crear_producto(
        descripcion,
        precio,
        existencias,
        unidad,
        imagen
    ):

        producto = Producto(
            descripcion=descripcion,
            precio=precio,
            existencias=existencias,
            unidad=unidad,
            imagen_de_producto=imagen
        )

        return producto_repository.insertar_producto(producto)


    # ==============================================
    # LISTAR PRODUCTOS
    # ==============================================

    @staticmethod
    def listar_productos():

        return producto_repository.obtener_productos()


    # ==============================================
    # BUSCAR PRODUCTO
    # ==============================================

    @staticmethod
    def buscar_producto(idproductos):

        return producto_repository.obtener_producto(idproductos)


    # ==============================================
    # MODIFICAR PRODUCTO
    # ==============================================

    @staticmethod
    def modificar_producto(
        idproductos,
        descripcion,
        precio,
        existencias,
        unidad,
        imagen
    ):

        producto = Producto(
            idproductos=idproductos,
            descripcion=descripcion,
            precio=precio,
            existencias=existencias,
            unidad=unidad,
            imagen_de_producto=imagen
        )

        return producto_repository.actualizar_producto(producto)


    # ==============================================
    # ELIMINAR PRODUCTO
    # ==============================================

    @staticmethod
    def borrar_producto(idproductos):

        return producto_repository.eliminar_producto(idproductos)

