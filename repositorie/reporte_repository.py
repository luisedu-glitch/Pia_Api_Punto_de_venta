
from config.database import get_conn

from models.reporte_model import (
    VentaPorCaja,
    VentaPorProducto
)


class ReporteRepository:

    # =========================================
    # REPORTE DE VENTAS POR CAJA
    # =========================================

    @staticmethod
    def obtener_ventas_por_caja():

        conn = get_conn()
        cur = conn.cursor()

        try:
            cur.execute("""
                SELECT
                    numero_caja,
                    nombre_caja,
                    total_ventas,
                    cantidad_tickets
                FROM vw_ReporteCaja
            """)

            filas = cur.fetchall()

            reportes = []

            for f in filas:
                reportes.append(
                    VentaPorCaja(
                        numero_de_caja=f[0],
                        nombre_caja=f[1],
                        total_ventas=f[2],
                        cantidad_tickets=f[3]
                    )
                )

            return reportes

        finally:
            cur.close()
            conn.close()


    # =========================================
    # REPORTE DE VENTAS POR PRODUCTO
    # =========================================

    @staticmethod
    def obtener_ventas_por_producto():

        conn = get_conn()
        cur = conn.cursor()

        try:
            cur.execute("""
                SELECT
                    idproductos,
                    descripcion,
                    cantidad_vendida,
                    total_generado
                FROM vw_ReporteProductos
            """)

            filas = cur.fetchall()

            reportes = []

            for f in filas:
                reportes.append(
                    VentaPorProducto(
                        idproductos=f[0],
                        descripcion=f[1],
                        cantidad_vendida=f[2],
                        total_generado=f[3]
                    )
                )

            return reportes

        finally:
            cur.close()
            conn.close()


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

