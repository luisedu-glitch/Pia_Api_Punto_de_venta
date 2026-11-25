from config.database import get_conn
from decimal import Decimal
from models.venta_model import Venta


class VentaRepository:

    # =====================================================
    # EJECUTAR SP Y OBTENER UN REGISTRO
    # =====================================================
    @staticmethod
    def _call_fetchone(cursor, sp, params):
        cursor.callproc(sp, params)

        resultado = None

        for result in cursor.stored_results():
            resultado = result.fetchone()

        return resultado


    # =====================================================
    # REGISTRAR VENTA
    # =====================================================
    @staticmethod
    def registrar_venta(
        id_usuario,
        numero_de_caja,
        productos,
        reporte,
        rango
    ):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        try:
            conn.start_transaction()

            total_venta = Decimal("0.00")
            detalles_procesados = []
            nombres_productos = []

            # 1. VALIDAR USUARIO
            usuario = VentaRepository._call_fetchone(
                cursor, "sp_venta_validar_usuario", [id_usuario]
            )

            if not usuario:
                raise Exception("El usuario no existe.")

            if usuario["status"] != 1:
                raise Exception("El usuario se encuentra inactivo.")

            # 2. VALIDAR CAJA
            caja = VentaRepository._call_fetchone(
                cursor, "sp_venta_validar_caja", [numero_de_caja]
            )

            if not caja:
                raise Exception("La caja no existe.")

            if caja["estatus"] != 1:
                raise Exception("La caja se encuentra inactiva.")

            # 3. VALIDAR PRODUCTOS
            for item in productos:

                id_prod = item["id_producto"]
                cant = int(item["cantidad"])

                if cant <= 0:
                    raise Exception("La cantidad debe ser mayor que cero.")

                prod = VentaRepository._call_fetchone(
                    cursor, "sp_venta_obtener_producto", [id_prod]
                )

                if not prod:
                    raise Exception(f"El producto con ID {id_prod} no existe.")

                if prod["status"] != 1:
                    raise Exception(f"El producto {id_prod} está inactivo.")

                if prod["existencias"] < cant:
                    raise Exception(
                        f"Existencias insuficientes para {prod['descripcion']}."
                    )

                precio_unitario = Decimal(str(prod["precio"]))
                importe = precio_unitario * cant
                total_venta += importe

                detalles_procesados.append({
                    "id_producto": id_prod,
                    "cantidad": cant,
                    # CAMBIO: float para que el JSON no falle con Decimal
                    "precio_unitario": float(precio_unitario)
                })

                nombres_productos.append(prod["descripcion"])

            # 4. DESCRIPCIÓN DE PRODUCTOS
            descripcion_productos = ", ".join(nombres_productos)[:45]

            # 5. CREAR VENTA
            resultado_venta = VentaRepository._call_fetchone(
                cursor,
                "sp_venta_crear",
                [
                    total_venta,
                    reporte,
                    rango,
                    numero_de_caja,
                    descripcion_productos,
                    id_usuario
                ]
            )

            if not resultado_venta:
                raise Exception("No se pudo obtener el ticket de la venta.")

            ticket = resultado_venta["ticket"]

            # 6. AGREGAR DETALLES
            for detalle in detalles_procesados:
                cursor.callproc(
                    "sp_venta_agregar_detalle",
                    [
                        ticket,
                        detalle["id_producto"],
                        detalle["cantidad"],
                        detalle["precio_unitario"]
                    ]
                )

                for result in cursor.stored_results():
                    result.fetchall()

            # 7. CONFIRMAR
            conn.commit()

            return {
                "ticket": ticket,
                "total": float(total_venta),
                "numero_de_caja": numero_de_caja,
                "productos": detalles_procesados
            }

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()