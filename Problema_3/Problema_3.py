import zipfile
import requests
import os

def descargar_imagen(url):
    try:
        response = requests.get(url)
        if response:
            os.makedirs('./Problema_3/Descargas')
            with open('./Problema_3/Descargas/imagen.jpg', 'wb') as image:
                image.write(response.content)
            print("¡Imagen descargada!")
    except:
        print("No se pudo descargar la imagen")

def almacenar_zip():
    try:
        with zipfile.ZipFile('./Problema_3/archivo.zip', 'w') as zip:
            zip.write('./Problema_3/Descargas/imagen.jpg', 'imagen.jpg')
            print("Imagen almacenada en un archivo .zip")
    except:
        print('No se pudo guardar la imagen en el archivo zip')

def extraer_zip():
    try:
        with zipfile.ZipFile('./Problema_3/archivo.zip', 'r') as zip:
            zip.extractall('./Problema_3/Unzip')
            print("Archivo .zip extraido")
    except:
        print("No se puedo extraer el archivo zip")

if __name__ == '__main__':
    url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    
    descargar_imagen(url)
    almacenar_zip()
    extraer_zip()