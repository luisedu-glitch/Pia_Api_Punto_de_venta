from repositorie import usuario_repository


class UsuarioService:
    @staticmethod
    def obtener_todos():
        return usuario_repository.UsuarioRepository.obtener_todos()

  
    @staticmethod
    def obtener_por_id(id_usuario):
        return usuario_repository.UsuarioRepository.obtener_por_id(id_usuario)

   
    @staticmethod
    def obtener_por_correo(correo):
        return usuario_repository.UsuarioRepository.obtener_por_correo(correo)

  
    @staticmethod
    def crear(datos):
        return usuario_repository.UsuarioRepository.crear(datos)

   
    @staticmethod
    def actualizar_usuario(id_usuario, datos):
        if not datos:
            return False

        return usuario_repository.UsuarioRepository.actualizar(
            id_usuario, datos
        )
    