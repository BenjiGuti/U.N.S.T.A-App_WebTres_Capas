import sqlite3

def conectar():
    return sqlite3.connect("productos.db")

def crear_tabla():
    conn = conectar()
    conn.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, descripcion TEXT, precio REAL)")
    conn.commit()
    conn.close()

def insertar(nombre, descripcion, precio):
    conn = conectar()
    conn.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)", (nombre, descripcion, precio))
    conn.commit()
    conn.close()
