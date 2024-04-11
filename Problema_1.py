import requests

def tasa_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        print("Datos no encontrados")

def saldo():
    while True:
        try:
            saldo = float(input("Ingrese la cantidad de BitCoin que posee: "))
            if saldo < 0:
                raise ValueError
            return saldo
        except:
            print("¡Ingrese un valor válido!")

if __name__ == '__main__':
    tasa_usd = tasa_bitcoin()
    saldo_bitcoin = saldo()

    conversion = tasa_usd * saldo_bitcoin

    print(f"Su saldo actual es: {saldo_bitcoin:,.4f} BTC")
    print(f"La tasa de hoy es: ${tasa_usd:,.4f}")
    print(f"La conversión es: ${conversion:,.4f}")