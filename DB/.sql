-- =====================================================
-- 2. TABLA PRODUCTOS
-- =====================================================

CREATE TABLE productos (
    idproductos INT NOT NULL AUTO_INCREMENT,
    descripcion VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    existencias INT NOT NULL,
    unidad VARCHAR(45) NOT NULL,
    imagen_de_producto MEDIUMBLOB NULL,
    status INT NOT NULL DEFAULT 1,
    PRIMARY KEY (idproductos)
);


-- =====================================================
-- 3. TABLA USUARIO
-- =====================================================

CREATE TABLE usuario (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    usuario VARCHAR(50) NOT NULL,
    Correo VARCHAR(50) NOT NULL,
    direccion VARCHAR(45) DEFAULT NULL,
    alias VARCHAR(45) NOT NULL,
    telefono VARCHAR(20) DEFAULT NULL,
    apellido VARCHAR(45) NOT NULL,
    fecha_de_nacimiento DATE NOT NULL,
    imagen_de_usuario MEDIUMBLOB NULL,
    contrasena VARCHAR(255) NOT NULL,
    status INT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_usuario),
    UNIQUE (Correo),
    UNIQUE (usuario)
);


-- =====================================================
-- 4. TABLA CAJA
-- =====================================================

CREATE TABLE caja (
    id_caja INT NOT NULL AUTO_INCREMENT,
    numero_caja INT NOT NULL UNIQUE,
    descripcion VARCHAR(100) NOT NULL,
    estatus INT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_caja)
);


-- =====================================================
-- 5. TABLA VENTA
-- =====================================================

CREATE TABLE venta (
    ticket INT NOT NULL AUTO_INCREMENT,
    total DECIMAL(10,2) NOT NULL,
    reporte VARCHAR(45) NOT NULL,
    Rango VARCHAR(45) NOT NULL,
    numero_de_caja INT NOT NULL,
    producto VARCHAR(45) NOT NULL,
    PRIMARY KEY (ticket),

    CONSTRAINT fk_venta_caja
    FOREIGN KEY (numero_de_caja)
    REFERENCES caja(numero_caja)
);


-- =====================================================
-- 6. TABLA USUARIO_VENTA
-- =====================================================

CREATE TABLE usuario_venta (
    id_usuario INT NOT NULL,
    ticket_venta INT NOT NULL,

    PRIMARY KEY (id_usuario, ticket_venta),

    CONSTRAINT fk_usuario_venta_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id_usuario),

    CONSTRAINT fk_usuario_venta_ticket
    FOREIGN KEY (ticket_venta)
    REFERENCES venta(ticket)
);


-- =====================================================
-- 7. TABLA DETALLE_VENTA
-- =====================================================

CREATE TABLE detalle_venta (
    id_detalle INT NOT NULL AUTO_INCREMENT,
    fk_detalle_ticket INT NOT NULL,
    ID_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (id_detalle),

    CONSTRAINT fk_detalle_venta_ticket
    FOREIGN KEY (fk_detalle_ticket)
    REFERENCES venta(ticket),

    CONSTRAINT fk_detalle_venta_producto
    FOREIGN KEY (ID_producto)
    REFERENCES productos(idproductos)
);