import sqlite3

def conectar():
    return sqlite3.connect("personas.db")

def crear_tabla():
    conn = conectar()
    conn.execute("CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, edad INTEGER)")
    conn.commit()
    conn.close()

def insertar(nombre, apellido, edad):
    conn = conectar()
    conn.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (?, ?, ?)", (nombre, apellido, edad))
    conn.commit()
    conn.close()
