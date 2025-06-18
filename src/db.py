import sqlite3
import datetime

# FUNCION CONEXION A BBDD
def conectar_db():
    conn = sqlite3.connect("bbdd/estacion.db")  # OJO: revisar el nombre correcto de la base
    return conn

# FUNCION LEER DATOS
def leer_datos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturas ORDER BY fecha_hora DESC LIMIT 10")
    datos = cursor.fetchall()
    conn.close()
    return datos

# FUNCION INSERTAR DATOS
def insertar_dato(temp, hum, presion, lux, velocidad):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO lecturas (fecha_hora, temperatura, humedad, presion, lux, velocidad_viento)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (datetime.datetime.now(), temp, hum, presion, lux, velocidad))
    conn.commit()
    conn.close()
