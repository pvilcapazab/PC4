import requests
import sqlite3

def tasa_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    tasa_cambio = []
    try:
        response = requests.get(url)
        if response:
            data = response.json()
            tasa_cambio.append(data['bpi']["USD"]["rate_float"])
            tasa_cambio.append(data['bpi']["GBP"]["rate_float"])
            tasa_cambio.append(data['bpi']["EUR"]["rate_float"])
            tasa_cambio.append(calcular_pen(data['bpi']['USD']['rate_float']))
            return tasa_cambio
    except:
        print("No se encontraron datos")

def crear_tablaBC():
    sentencia = """CREATE TABLE IF NOT EXISTS bitcoin(
        USD REAL,
        GBP REAL,
        EUR REAL,
        PEN REAL);"""
    try:
        with sqlite3.connect("./Problema_7/base.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sentencia)
            conn.commit()
        print("Tabla creada")
    except:
        print("No se pudo crear la tabla")

def insertar_datos(datos):
    sentencia = """INSERT INTO bitcoin(USD, GBP, EUR, PEN) VALUES (?, ?, ?, ?)"""
    try:
        with sqlite3.connect("./Problema_7/base.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sentencia, datos)
        print("Datos insertados en la tabla")
    except:
        print("No se encontró la tabla")

def calcular_pen(dolar):
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    try:
        response = requests.get(url)
        data = response.json()
    except:
        print("No se encontraron datos")
    pen = round(dolar * data["compra"], 4)
    return pen

def mostrar_tabla():
    try:
        with sqlite3.connect("./Problema_7/base.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bitcoin")
            monedas = cursor.fetchall()
            for moneda in monedas:
                print(moneda)
    except:
        print("No se encontró la tabla")

if __name__ == '__main__':
    crear_tablaBC()
    data = tasa_bitcoin()
    insertar_datos(data)
    mostrar_tabla()