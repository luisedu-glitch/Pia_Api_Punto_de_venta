from models.venta_model import Venta
from repositorie import venta_repository


class VentaService:

    @staticmethod
    def realizar_venta(datos):

        if not datos:
            return None, "No se recibieron datos de la venta", 400

        id_usuario = datos.get("id_usuario")
        numero_de_caja = datos.get("numero_de_caja")
        productos = datos.get("productos", [])
        reporte = datos.get("reporte")
        rango = datos.get("rango")

        # Validar datos obligatorios
        if (
            id_usuario is None
            or numero_de_caja is None
            or not productos
            or reporte is None
            or rango is None
        ):
            return None, "Parámetros incompletos en la solicitud", 400

        try:
            # CAMBIO: se llama a la clase VentaRepository
            resultado = venta_repository.VentaRepository.registrar_venta(
                id_usuario,
                numero_de_caja,
                productos,
                reporte,
                rango
            )

            return resultado, "Venta registrada correctamente", 201

        except Exception as e:

            msg = str(e)

            if "Existencias insuficientes" in msg:
                return None, msg, 400

            if "inactivo" in msg.lower():
                return None, msg, 400

            if "no existe" in msg.lower():
                return None, msg, 404

            if "cantidad" in msg.lower():
                return None, msg, 400

            return None, msg, 500