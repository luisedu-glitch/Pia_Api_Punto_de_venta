from models.venta_model import Venta
from repositorie import venta_repository

class VentaService:
    @staticmethod
    def realizar_venta(datos):
        id_usuario = datos.get('id_usuario')
        id_caja = datos.get('id_caja')
        productos = datos.get('productos', [])

        if not id_usuario or not id_caja or not productos:
            return None, "Parámetros incompletos en la solicitud", 400

        try:
            resultado = venta_repository.registrar_venta(id_usuario, id_caja, productos)
            return resultado, "Venta registrada correctamente", 201
        except Exception as e:
            msg = str(e)
            if "Existencias insuficientes" in msg:
                return None, "Existencias insuficientes", 400
            return None, msg, 500