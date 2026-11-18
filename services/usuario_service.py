from models.usuario_model import Usuario
from repositorie import usuario_repository

class UsuarioService:

    @staticmethod
    def obtener_todos():
        return usuario_repository.obtener_todos()

    @staticmethod
    def obtener_por_id(id_usuario):
        return usuario_repository.obtener_por_id(id_usuario)

    @staticmethod
    def actualizar_usuario(id_usuario, datos):
        return usuario_repository.actualizar(id_usuario, datos)