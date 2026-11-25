Documentación del Proyecto: API REST Punto de Venta
Universidad Autónoma de Nuevo León
Facultad de Ciencias Físico Matemáticas
Materia: Interfaz de programación de aplicaciones
Profesor: Juan Alejandro Villarreal Mojica
Alumno: Luis Eduardo Ruiz Quintanar
Grupo: 51
Avance: 3er Avance

1. Descripción del Proyecto
Desarrollo de una API REST para el manejo de un punto de venta utilizando Python, Flask y MySQL. La aplicación permite el registro de usuarios (con imagen), inicio de sesión seguro con tokens, registro y modificación de productos, gestión de ventas y consultas/reportes de ventas.
2. Tecnologías utilizadas
- `Python`: Lenguaje de programación principal.
- `Flask`: Micro-framework web utilizado para construir la API REST.
- `MySQL`: Sistema de gestión de bases de datos relacional.
- `Flask-JWT-Extended`: Extensión para la autenticación y generación de Tokens (JWT).
- `mysql-connector-python`: Conector oficial para enlazar Python con la base de datos MySQL.
- `Postman`: Software utilizado para probar y documentar los endpoints de la API.
3.  Requerimientos
- `Python 3.8 o superior` 
- `MySQL Server` 
- `pip` 
4. instalaciones
- `Flask`: `pip install Flask` 
- `Flask-JWT-Extended`: `pip install Flask-JWT-Extended` 
- `mysql-connector-python`: `pip install mysql-connector-python`
- `python-dotenv`: `pip install python-dotenv`  
5. Diseño de la Base de Datos

El proyecto cuenta con las siguientes tablas principales en MySQL:

- **`usuario`**: `id_usuario`, `usuario`, `correo`, `direccion`, `alias`, `telefono`, `apellido`, `fecha_nacimiento`, `imagen_de_usuario`, `contraseña`, `status`.
- **`productos`**: `idproductos`, `descripcion`, `precio`, `existencias`, `unidad`, `imagen_de_producto`, `status`.
- **`caja`**: `id_caja`, `numero_caja`, `descripcion`, `estatus`.
- **`venta`**: `ticket`, `total`, `reporte`, `Rango`, `numero_de_caja`, `producto`.
- **`detalle_venta`**: `id_detalle`, `fk_detalle_ticket`, `id_producto`, `cantidad`, `precio_unitario`.
- **`usuario_venta`**: Tabla intermedia para relacionar usuarios y ventas.
6. Arquitectura y Estructura del Proyecto
PIA_API/
├── .venv/                  # Entorno virtual de Python
├── config/                 # Configuración del proyecto y base de datos
├── controller/             # Capa de controladores (manejo de peticiones HTTP)
│   ├── auth_controller.py
│   ├── producto_controller.py
│   ├── reporte_controller.py
│   ├── usuario_controller.py
│   └── venta_controller.py
├── DB/                     # Scripts o conexión a la base de datos
├── models/                 # Capa de modelos (estructura de los datos)
│   ├── producto_model.py
│   ├── reporte_model.py
│   ├── usuario_model.py
│   └── venta_model.py
├── repositorie/            # Capa de repositorios (consultas SQL a la BD)
│   ├── producto_repository.py
│   ├── reporte_repository.py
│   ├── usuario_repository.py
│   └── venta_repository.py
├── servicios/              # Capa de servicios (lógica de negocio)
│   ├── producto_service.py
│   ├── reporte_service.py
│   ├── usuario_service.py
│   └── venta_service.py
├── .env                    # Variables de entorno (credenciales protegidas)
├── .gitignore              # Archivos ignorados por Git
├── app.py                  # Punto de entrada de la aplicación Flask
└── README.md               # Documentación del proyecto
7. Uso
## Endpoints de la API

A continuación se detallan los endpoints implementados en la API, indicando el método HTTP, la ruta, su función y si requieren autenticación mediante Token (JWT).

### Autenticación 
*   `POST /login`: Inicia sesión con correo y contraseña. Devuelve el token de acceso (JWT). *(No requiere Token)*

### Gestión de Usuarios 
*   `GET /usuarios`: Obtiene la lista de todos los usuarios registrados. *(Requiere Token)*
*   `GET /usuarios/{id_usuario}`: Obtiene un usuario específico por su ID. *(Requiere Token)*
*    `POST/usuarios `:Registra un nuevo usuario (sporta imagen)  *(Requiere Token)*
*   `PUT /usuarios/{id_usuario}`: Actualiza los datos de un usuario existente. *(Requiere Token)*

### Gestión de Productos 
*   `GET /productos`: Obtiene la lista de todos los productos. *(No requiere Token)*
*   `GET /productos/{idproductos}`: Obtiene un producto por su ID. *(No requiere Token)*
*   `POST /productos`: Registra un nuevo producto (soporta subida de imagen y valida precio/existencias). *(Requiere Token)*
*   `PUT /productos/{idproductos}`: Modifica los datos de un producto existente. *(Requiere Token)*
*   `DELETE /productos/{idproductos}`: Elimina un producto del sistema. *(Requiere Token)*

### Gestión de Ventas
*   `POST /ventas`: Registra una nueva venta en el sistema. *(Requiere Token)*

### Reportes 
*   `GET /reportes/caja/{numero_caja}/total`: Obtiene el total de ventas generadas por una caja específica. *(No requiere Token)*
*   `GET /reportes/producto/{idproducto}/total`: Obtiene el total generado por un producto específico. *(No requiere Token)*