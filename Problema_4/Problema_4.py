import requests

def tasa_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    datos_bitcoin = []
    try:
        response = requests.get(url)
        data = response.json()
        datos_bitcoin.append(data["bpi"]["USD"])
        datos_bitcoin.append(data["bpi"]["GBP"])
        datos_bitcoin.append(data["bpi"]["EUR"])
        return datos_bitcoin
    except requests.RequestException:
        print("Datos no encontrados")

def archivo_txt(datos):
    try:
        with open('./Problema_4/Datos_BitCoin.txt', 'w') as file:
            for dato in datos:
                file.write(f'Precio en {dato["code"]}: {dato["rate_float"]}\n')
            print("Archivo .txt creado con éxito")
    except:
        print("Ocurrió un error mientras escribiamos en el archivo")

if __name__ == '__main__':
    datos = tasa_bitcoin()
    archivo_txt(datos)