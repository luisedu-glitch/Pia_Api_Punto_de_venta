CREATE TABLE `productos` (
  `idproductos` date NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `precio` date NOT NULL,
  `existencias` date NOT NULL,
  `unidad` date NOT NULL,
  `imagen_de_producto` varchar(45) NOT NULL,
  PRIMARY KEY (`idproductos`)
);

CREATE TABLE `usuario` (
  `Correo` varchar(50) NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `alias` varchar(45) NOT NULL,
  `telefono` date DEFAULT NULL,
  `apelldio` varchar(45) NOT NULL,
  `fecha_de_nacimiento` date NOT NULL,
  `imagen_de_usuario` blob NOT NULL,
  `contrasena` varchar(50) NOT NULL,
  PRIMARY KEY (`Correo`)
);

CREATE TABLE `usuario_venta` (
  `correo_usuario` varchar(50) NOT NULL,
  `ticket_venta` date NOT NULL,
  KEY `correo_usuario_idx` (`correo_usuario`),
  KEY `ticket_venta_idx` (`ticket_venta`),
  CONSTRAINT `correo_usuario` 
	  FOREIGN KEY (`correo_usuario`)
           REFERENCES `usuario` (`Correo`),
  CONSTRAINT `ticket_venta` 
		FOREIGN KEY (`ticket_venta`) 
				REFERENCES `venta` (`ticket`)
);

CREATE TABLE `venta` (
  `ticket` date NOT NULL,
  `total` date NOT NULL,
  `reporte` varchar(45) NOT NULL,
  `Rango` date NOT NULL,
  `numero_de_caja` date NOT NULL,
  `producto` varchar(45) NOT NULL,
  PRIMARY KEY (`ticket`)
);

CREATE TABLE `detalle_venta` (
  `fk_detalle_ticket` date NOT NULL,
  `ID_producto` date NOT NULL,
  `cantidad` date NOT NULL,
  `precio_unitario` date NOT NULL,
  KEY `ticket_venta_idx` (`fk_detalle_ticket`),
  KEY `ID_producto_idx` (`ID_producto`),
  CONSTRAINT `fk_detalle_ticket` FOREIGN KEY (`fk_detalle_ticket`) REFERENCES `venta` (`ticket`),
  CONSTRAINT `ID_producto` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`idproductos`)
);