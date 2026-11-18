class Usuario:
    def __init__(
        self,
        id_usuario=None,
        nombre=None,
        apellido=None,
        Correo=None,
        contrasena=None,
        telefono=None,
        direccion=None,
        imagen=None,
        nickname=None,
        fecha_nacimiento=None,
        status=1
    ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.Correo = Correo
        self.contrasena = contrasena
        self.telefono = telefono
        self.direccion = direccion
        self.imagen = imagen
        self.nickname = nickname
        self.fecha_nacimiento = fecha_nacimiento
        self.status = status