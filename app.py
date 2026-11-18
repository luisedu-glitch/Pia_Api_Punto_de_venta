from flask import Flask
from flask_jwt_extended import JWTManager
from Controller.auth_controller import auth_bp
from Controller.producto_controller import producto_bp
from Controller.reporte_controller import reporte_bp
from Controller.usuario_controller import usuario_bp
from Controller.venta_controller import venta_bp


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(producto_bp)
app.register_blueprint(reporte_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(venta_bp)

if __name__ == "__main__":
    app.run(debug=True)