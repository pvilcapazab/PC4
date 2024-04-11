def contar_lineas(archivo):
    try:
        with open(archivo, 'r') as file:
            contador = 0
            lineas = file.readlines()
            for linea in lineas:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                contador +=1
            print(f"El archivo contiene: {contador} líneas")
    except FileNotFoundError:
        print("---Archivo no encontrado---")

def ruta_archivo_py():
    while True:
        ruta = input("Ingrese la ruta de su archivo:\n")
        if ruta.endswith(".py"):
            return ruta
        else:
            print("---El archivo debe terminar en .py---")

if __name__ == '__main__':
    ruta = ruta_archivo_py()
    contar_lineas(ruta)