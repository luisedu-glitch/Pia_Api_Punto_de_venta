from config.database import get_conn
from models.usuario_model import Usuario

class UsuarioRepository:
    @staticmethod
    def obtener_por_correo(Correo):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE Correo = %s", (Correo,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario

    @staticmethod
    def obtener_por_id(id_usuario):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id_usuario, nombre, apellido, Correo, telefono,
                   direccion, nickname, fecha_nacimiento, status
            FROM usuario WHERE id_usuario = %s
        """, (id_usuario,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario

    @staticmethod
    def obtener_todos():
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id_usuario, nombre, apellido, Correo, telefono,
                   direccion, nickname, fecha_nacimiento, status
            FROM usuario
        """)
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios

    @staticmethod
    def crear(datos):
        conn = get_conn()
        cursor = conn.cursor()
        query = """
            INSERT INTO usuario (nombre, apellido, Correo, contrasena, telefono, direccion, nickname, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            datos.get('nombre'), datos.get('apellido'), datos.get('Correo'),
            datos.get('contrasena'), datos.get('telefono'), datos.get('direccion'),
            datos.get('nickname'), datos.get('fecha_nacimiento')
        )
        cursor.execute(query, params)
        conn.commit()
        id_creado = cursor.lastrowid
        cursor.close()
        conn.close()
        return id_creado

    @staticmethod
    def actualizar(id_usuario, datos):
        conn = get_conn()
        cursor = conn.cursor()
        query = """
            UPDATE usuario
            SET nombre = %s, apellido = %s, telefono = %s, direccion = %s, nickname = %s
            WHERE id_usuario = %s
        """
        params = (
            datos.get('nombre'), datos.get('apellido'), datos.get('telefono'),
            datos.get('direccion'), datos.get('nickname'), id_usuario
        )
        cursor.execute(query, params)
        conn.commit()
        filas = cursor.rowcount
        cursor.close()
        conn.close()
        return filas > 0