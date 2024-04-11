from pyfiglet import Figlet
import random

figlet = Figlet()
fuentes = figlet.getFonts()

def display():
    while True:
        fuente = input(f"{'=' * 100}\nIntroduce la fuente que desea utilizar (Si no introduce nada, se eligirá uno): ")
        if fuente == "":
            figlet.setFont(font=fuentes[random.randint(0, 548)])
            break
        elif fuente in fuentes:
            figlet.setFont(font=fuente)
            break
        else:
            print("Fuente no encontrada")

    texto_imprimir = input("Ingrese el texto:\n")

    print("\n", figlet.renderText(texto_imprimir))

if __name__ == '__main__':
    display()