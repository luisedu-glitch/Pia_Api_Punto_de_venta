
class VentaPorCaja:

    def __init__(
        self,
        numero_de_caja=None,
        nombre_caja=None,
        total_ventas=None,
        cantidad_tickets=None
    ):

        self.numero_de_caja = numero_de_caja
        self.nombre_caja = nombre_caja
        self.total_ventas = total_ventas
        self.cantidad_tickets = cantidad_tickets

    def a_diccionario(self):

        return {
            "numero_de_caja": self.numero_de_caja,
            "nombre_caja": self.nombre_caja,
            "total_ventas": float(self.total_ventas)
            if self.total_ventas is not None else None,
            "cantidad_tickets": self.cantidad_tickets
        }


class VentaPorProducto:

    def __init__(
        self,
        idproductos=None,
        descripcion=None,
        cantidad_vendida=None,
        total_generado=None
    ):

        self.idproductos = idproductos
        self.descripcion = descripcion
        self.cantidad_vendida = cantidad_vendida
        self.total_generado = total_generado

    def a_diccionario(self):

        return {
            "idproductos": self.idproductos,
            "descripcion": self.descripcion,
            "cantidad_vendida": self.cantidad_vendida,
            "total_generado": float(self.total_generado)
            if self.total_generado is not None else None
        }
