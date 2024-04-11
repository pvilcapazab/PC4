import requests
import sqlite3

def tipo_cambio():
    compra_venta = []
    for i in range(1, 13):
        url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={i}&year=2023'
        try:
            response = requests.get(url)
            if response:
                data = response.json()
                compra_venta.extend(data)
        except:
            print(f"Sucedió un error en el mes {i}")
    return compra_venta

def crear_tabla():
    sentencia = """
    CREATE TABLE IF NOT EXISTS sunat_info(
        compra REAL,
        venta REAL,
        moneda TEXT,
        fecha TEXT);"""
    try:
        with sqlite3.connect('./Problema_7/base.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sentencia)
            conn.commit()
        print("Tabla creada")
    except:
        print("Error al crear la tabla")

def insertar_tabla(datos):
    try:
        with sqlite3.connect("./Problema_7/base.db") as conn:
            cursor = conn.cursor()
            sentencia = """INSERT INTO sunat_info(compra, venta, moneda, fecha) VALUES (?, ?, ?, ?)"""
            for dato in datos:
                cursor.execute(sentencia, (dato["compra"], dato["venta"], dato["moneda"], dato["fecha"]))
            conn.commit()
        print("Datos insertados en la tabla")
    except:
        print("Ha ocurrido un problema")

def mostrar_tabla():
    try:
        with sqlite3.connect("./Problema_7/base.db") as conn:
            cursos = conn.cursor()
            cursos.execute("SELECT * FROM sunat_info")
            monedas = cursos.fetchall()
            for moneda in monedas:
                print(moneda)
    except:
        print("No se encontró la tabla")

if __name__ == '__main__':
    data = tipo_cambio()
    crear_tabla()
    insertar_tabla(data)
    mostrar_tabla()