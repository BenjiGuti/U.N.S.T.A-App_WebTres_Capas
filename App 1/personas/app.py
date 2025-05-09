from flask import Flask, request, render_template
from acceso_datos import persona_db
from logica_negocio import servicios

app = Flask(__name__)
persona_db.crear_tabla()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    edad = int(request.form["edad"])
    if servicios.validar_persona(nombre, apellido, edad):
        persona_db.insertar(nombre, apellido, edad)
    return "Persona agregada"

if __name__ == "__main__":
    app.run(debug=True)
