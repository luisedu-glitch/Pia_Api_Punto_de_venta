
from config.database import get_conn
from models.producto_model import Producto


class Productorepository:

    # ==============================================
    # INSERTAR PRODUCTO
    # ==============================================

    @staticmethod
    def insertar_producto(producto):

        conn = get_conn()
        cur = conn.cursor(buffered=True)

        try:
            sql = """
                CALL sp_Productos(
                    %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """

            valores = (
                'I',
                None,
                producto.descripcion,
                producto.precio,
                producto.existencias,
                producto.unidad,
                producto.imagen_de_producto,
                1
            )

            cur.execute(sql, valores)
            resultado = cur.fetchone()

            while cur.nextset():
                pass

            if resultado is None:
                raise Exception("No se obtuvo el ID del producto")

            producto.idproductos = resultado[0]

            conn.commit()
            return producto

        except Exception as e:
            conn.rollback()
            print("Error al insertar producto:", e)
            raise

        finally:
            cur.close()
            conn.close()


    # ==============================================
    # LISTAR PRODUCTOS MEDIANTE VISTA
    # ==============================================

    @staticmethod
    def obtener_productos():

        conn = get_conn()
        cur = conn.cursor(buffered=True)

        try:
            cur.execute("""
                SELECT
                    idproductos,
                    descripcion,
                    precio,
                    existencias,
                    unidad,
                    imagen_de_producto,
                    status
                FROM vw_ProductosActivos
            """)

            filas = cur.fetchall()
            productos = []

            for fila in filas:

                producto = Producto(
                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6]
                )

                productos.append(producto)

            return productos

        finally:
            cur.close()
            conn.close()


    # ==============================================
    # BUSCAR PRODUCTO POR ID
    # ==============================================

    @staticmethod
    def obtener_producto(idproductos):

        conn = get_conn()
        cur = conn.cursor(buffered=True)

        try:
            sql = """
                CALL sp_Productos(
                    %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """

            valores = (
                'S',
                idproductos,
                None, None, None, None, None, None
            )

            cur.execute(sql, valores)
            fila = cur.fetchone()

            while cur.nextset():
                pass

            if fila is None:
                return None

            return Producto(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6]
            )

        finally:
            cur.close()
            conn.close()


    # ==============================================
    # ACTUALIZAR PRODUCTO
    # ==============================================

    @staticmethod
    def actualizar_producto(producto):

        conn = get_conn()
        cur = conn.cursor(buffered=True)

        try:
            sql = """
                CALL sp_Productos(
                    %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """

            valores = (
                'U',
                producto.idproductos,
                producto.descripcion,
                producto.precio,
                producto.existencias,
                producto.unidad,
                producto.imagen_de_producto,
                None
            )

            cur.execute(sql, valores)

            while cur.nextset():
                pass

            conn.commit()

            cur.execute("""
                SELECT idproductos
                FROM productos
                WHERE idproductos = %s
                AND status = 1
            """, (producto.idproductos,))

            return cur.fetchone() is not None

        except Exception as e:
            conn.rollback()
            print("Error al actualizar producto:", e)
            raise

        finally:
            cur.close()
            conn.close()


    # ==============================================
    # ELIMINAR PRODUCTO
    # ==============================================

    @staticmethod
    def eliminar_producto(idproductos):

        conn = get_conn()
        cur = conn.cursor(buffered=True)

        try:
            cur.execute("""
                SELECT idproductos
                FROM productos
                WHERE idproductos = %s
                AND status = 1
            """, (idproductos,))

            existe = cur.fetchone()

            if existe is None:
                return False

            sql = """
                CALL sp_Productos(
                    %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """

            valores = (
                'E',
                idproductos,
                None, None, None, None, None, None
            )

            cur.execute(sql, valores)

            while cur.nextset():
                pass

            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            print("Error al eliminar producto:", e)
            raise

        finally:
            cur.close()
            conn.close()

