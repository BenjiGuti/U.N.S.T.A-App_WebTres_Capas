from flask import Flask, request, render_template
from acceso_datos import producto_db
from logica_negocio import servicios

app = Flask(__name__)
producto_db.crear_tabla()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = float(request.form["precio"])
    if servicios.validar_producto(nombre, descripcion, precio):
        producto_db.insertar(nombre, descripcion, precio)
    return "Producto agregado"

if __name__ == "__main__":
    app.run(debug=True)
