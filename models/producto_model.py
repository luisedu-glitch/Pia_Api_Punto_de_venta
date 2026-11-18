
import base64


class Producto:

    def __init__(
        self,
        idproductos=None,
        descripcion=None,
        precio=None,
        existencias=None,
        unidad=None,
        imagen_de_producto=None,
        status=1
    ):

        self.idproductos = idproductos
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.unidad = unidad
        self.imagen_de_producto = imagen_de_producto
        self.status = status

    def a_lista(self):

        imagen = None

        if self.imagen_de_producto:
            imagen = base64.b64encode(
                self.imagen_de_producto
            ).decode("utf-8")

        return {
            "idproductos": self.idproductos,
            "descripcion": self.descripcion,
            "precio": float(self.precio) if self.precio is not None else None,
            "existencias": self.existencias,
            "unidad": self.unidad,
            "imagen_de_producto": imagen,
            "status": self.status
        }
