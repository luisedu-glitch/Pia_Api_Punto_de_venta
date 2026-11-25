import base64

from config.database import get_conn
from models.usuario_model import Usuario


def _imagen_a_base64(usuario):
    """Convierte la imagen binaria (MEDIUMBLOB) a texto base64 para el JSON."""
    img = usuario.get("imagen_de_usuario")
    usuario["imagen"] = base64.b64encode(img).decode("utf-8") if img else None
    usuario.pop("imagen_de_usuario", None)


class UsuarioRepository:

    # =====================================================
    # USUARIO POR CORREO
    # =====================================================
    @staticmethod
    def obtener_por_correo(Correo):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.callproc("sp_usuario_por_correo", [Correo])

            usuario = None

            for result in cursor.stored_results():
                usuario = result.fetchone()

            return usuario

        finally:
            cursor.close()
            conn.close()


    # =====================================================
    # USUARIO POR ID
    # =====================================================
    @staticmethod
    def obtener_por_id(id_usuario):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.callproc("sp_usuario_por_id", [id_usuario])

            usuario = None

            for result in cursor.stored_results():
                usuario = result.fetchone()

            if usuario:
                usuario["nombre"] = usuario.pop("usuario")
                usuario["nickname"] = usuario.pop("alias")
                usuario["fecha_nacimiento"] = usuario.pop(
                    "fecha_de_nacimiento"
                )
                _imagen_a_base64(usuario)

            return usuario

        finally:
            cursor.close()
            conn.close()


    # =====================================================
    # LISTAR USUARIOS
    # =====================================================
    @staticmethod
    def obtener_todos():
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.callproc("sp_usuario_listar")

            usuarios = []

            for result in cursor.stored_results():
                usuarios = result.fetchall()

            for usuario in usuarios:
                usuario["nombre"] = usuario.pop("usuario")
                usuario["nickname"] = usuario.pop("alias")
                usuario["fecha_nacimiento"] = usuario.pop(
                    "fecha_de_nacimiento"
                )
                _imagen_a_base64(usuario)

            return usuarios

        finally:
            cursor.close()
            conn.close()


    # =====================================================
    # CREAR USUARIO
    # =====================================================
    @staticmethod
    def crear(datos):
        conn = get_conn()
        cursor = conn.cursor()

        try:
            cursor.callproc("sp_usuario_crear", [
                datos.get("nombre"),
                datos.get("Correo"),
                datos.get("direccion"),
                datos.get("nickname"),
                datos.get("telefono"),
                datos.get("apellido"),
                datos.get("fecha_nacimiento"),
                datos.get("imagen"),
                datos.get("contrasena")
            ])

            id_creado = None

            for result in cursor.stored_results():
                resultado = result.fetchone()

                if resultado:
                    id_creado = resultado[0]

            conn.commit()

            return id_creado

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()


    # =====================================================
    # ACTUALIZAR USUARIO
    # =====================================================
    @staticmethod
    def actualizar(id_usuario, datos):
        conn = get_conn()
        cursor = conn.cursor()

        # Campo de la API -> columna real en MySQL
        campos = {
            "nombre": "usuario",
            "apellido": "apellido",
            "Correo": "Correo",
            "telefono": "telefono",
            "direccion": "direccion",
            "nickname": "alias",
            "fecha_nacimiento": "fecha_de_nacimiento",
            "imagen": "imagen_de_usuario",
            "status": "status",
            "contrasena": "contrasena"
        }

        try:
            conn.start_transaction()

            for campo_api, campo_bd in campos.items():
                if campo_api in datos:
                    cursor.callproc(
                        "sp_usuario_actualizar_campo",
                        [id_usuario, campo_bd, datos[campo_api]]
                    )
                    # Liberar resultados del CALL
                    for result in cursor.stored_results():
                        result.fetchall()

            conn.commit()
            return True

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()