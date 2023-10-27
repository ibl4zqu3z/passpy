import subprocess

def mostrar_banner():
    try:
        with open("banner.txt", "r") as archivo:
            banner = archivo.read()
            print(banner)
    except FileNotFoundError:
        print("Banner no encontrado.")

def mostrar_menu():
    print("Menú:")
    print("1. Opción 1: Toma de datos")
    print("2. Opción 2: Visualizar archivo de datos")
    print("3. Opción 3: Generar password desde archivo de datos")
    print("3. Opción 4: Generar password aleatoria sin datos")
    print("0. Salir")

def opcion_1():
    print("Has seleccionado la Opción 1")
    try:
        # Llamar al programa "dame_datos" usando subprocess
        subprocess.run(["python", "dame_datos.py"])
    except FileNotFoundError:
        print("El programa 'dame_datos.py' no se encuentra en el mismo directorio.")

def opcion_2():
    print("Has seleccionado la Opción 2")

def opcion_3():
    print("Has seleccionado la Opción 3")

def opcion_4():
    print("Has seleccionado la Opción 4")

mostrar_banner()

while True:
    mostrar_menu()
    seleccion = input("Selecciona una opción: ")

    if seleccion == "1":
        opcion_1()
    elif seleccion == "2":
        opcion_2()
    elif seleccion == "3":
        opcion_3()
    elif seleccion == "4":
        opcion_3()
    elif seleccion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida del menú.")
