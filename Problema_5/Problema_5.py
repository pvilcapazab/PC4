class Tabla:
    def __init__(self, n):
        self.n = n

    def crear_tabla(self):
        try:
            with open(f'./Problema_5/tabla-{self.n}.txt', 'w') as file:
                for i in range(1, 13):
                    file.write(f"{self.n} x {i} = {self.n * i}\n")
                print("¡Tabla creada!")
        except:
            print("¡Ha ocurrido un error!")

    def mostrar_tabla(self):
        try:
            with open(f"./Problema_5/tabla-{self.n}.txt", 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print("Tabla no encontrada")

    def mostrar_linea(self, m):
        try:
            with open(f"./Problema_5/tabla-{self.n}.txt", 'r') as file:
                lineas = file.readlines()
                if len(lineas) >= m:
                    print(lineas[m - 1])
                else:
                    raise ValueError
        except (FileNotFoundError, ValueError):
            print("No se encontró la línea")

def numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero en el rango de 1 a 10: "))
            if 1 <= numero <= 10:
                return numero
            else:
                raise ValueError
        except:
            print("Número inválido")

def display():
    menu = """===========================
Menú:
1) Crear tabla
2) Mostrar tabla
3) Mostrar línea de la tabla
4) Salir
==========================="""
    while True:
        print(menu)
        opcion = input()
        if opcion == '1':
            n = numero()
            Tabla(n).crear_tabla()
        elif opcion == '2':
            n = numero()
            data = Tabla(n).mostrar_tabla()
            if data != None:
                print(data)
        elif opcion == '3':
            print("---Número de tabla---")
            n = numero()
            if Tabla(n).mostrar_tabla():
                print("---Número de línea---")
                m = numero()
                Tabla(n).mostrar_linea(m)
        elif opcion == '4':
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    display()