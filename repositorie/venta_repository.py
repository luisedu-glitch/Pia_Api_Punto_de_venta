from config.database import get_conn
import uuid
from models.venta_model import Venta

class VentaRepository:
    @staticmethod
    def registrar_venta(id_usuario, id_caja, productos):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)
        try:
            conn.start_transaction()

            total_venta = 0
            detalles_procesados = []

            for item in productos:
                id_prod = item['id_producto']
                cant = item['cantidad']

                cursor.execute("SELECT id_producto, precio, existencias FROM productos WHERE id_producto = %s FOR UPDATE", (id_prod,))
                prod = cursor.fetchone()

                if not prod:
                    raise Exception(f"El producto con ID {id_prod} no existe.")
                if prod['existencias'] < cant:
                    raise Exception("Existencias insuficientes")

                precio_unitario = float(prod['precio'])
                importe = precio_unitario * cant
                total_venta += importe

                detalles_procesados.append({
                    'id_producto': id_prod,
                    'cantidad': cant,
                    'precio_unitario': precio_unitario,
                    'importe': importe,
                    'nuevas_existencias': prod['existencias'] - cant
                })

            folio = f"V-{uuid.uuid4().hex[:8].upper()}"
            query_venta = """
                INSERT INTO ventas (folio, id_usuario, id_caja, fecha_venta, total)
                VALUES (%s, %s, %s, NOW(), %s)
            """
            cursor.execute(query_venta, (folio, id_usuario, id_caja, total_venta))
            id_venta = cursor.lastrowid

            query_detalle = """
                INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario, importe)
                VALUES (%s, %s, %s, %s, %s)
            """
            query_stock = "UPDATE productos SET existencias = %s WHERE id_producto = %s"

            for d in detalles_procesados:
                cursor.execute(query_detalle, (id_venta, d['id_producto'], d['cantidad'], d['precio_unitario'], d['importe']))
                cursor.execute(query_stock, (d['nuevas_existencias'], d['id_producto']))

            conn.commit()
            return {"id_venta": id_venta, "folio": folio, "total": total_venta}

        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()