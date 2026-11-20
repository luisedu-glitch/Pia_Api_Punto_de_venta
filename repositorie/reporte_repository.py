
from config.database import get_conn

from models.reporte_model import (
    VentaPorCaja,
    VentaPorProducto
)


class ReporteRepository:
    # =========================================
    # FUNCION: TOTAL VENTAS POR CAJA
    # =========================================

    @staticmethod
    def obtener_total_ventas_caja(numero_caja):

        conn = get_conn()
        cur = conn.cursor()

        try:
            cur.execute(
                "SELECT fn_TotalVentasCaja(%s)",
                (numero_caja,)
            )

            resultado = cur.fetchone()

            return resultado[0] if resultado else 0

        finally:
            cur.close()
            conn.close()


    # =========================================
    # FUNCION: TOTAL GENERADO POR PRODUCTO
    # =========================================

    @staticmethod
    def obtener_total_generado_producto(idproducto):

        conn = get_conn()
        cur = conn.cursor()

        try:
            cur.execute(
                "SELECT fn_TotalGeneradoProducto(%s)",
                (idproducto,)
            )

            resultado = cur.fetchone()

            return resultado[0] if resultado else 0

        finally:
            cur.close()
            conn.close()

