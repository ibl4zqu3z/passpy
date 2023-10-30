# Crear un diccionario para almacenar los datos personales
datos_personales = {}

# Solicitar al usuario que ingrese los datos
datos_personales['nombre'] = input("Ingresa el nombre: ")
datos_personales['apellido1'] = input("Ingresa el primer apellido: ")
datos_personales['apellido2'] = input("Ingresa el segundo apellido: ")
datos_personales['ano_nacimiento'] = input("Ingresa la fecha de nacimiento: (DD/MM/AAAA) ")
#datos_personales['email'] = input("Ingresa tu dirección de correo electrónico: ")
datos_personales['telefono'] = input("Ingresa el número de teléfono: ")
if (input("¿Tiene mascota? S/N")) in ["S","si","s","SI"]: 
    datos_personales['nombre_mascota'] = input("Ingresa el nombre de la mascota: ")
if (input("¿TIene pareja o esta casado? S/N"))in ["S","si","s","SI"]:    
    datos_personales['nombre_pareja'] = input("Ingresa el nombre de mujer: ")
    datos_personales['aniversario'] = input("Ingresa la fecha de tu aniversario (DD/MM/AAAA): ")
datos_personales['equipo_futbol'] = input("Ingresa el equipo de fútbol favorito: ")
datos_personales['musica'] = input("Ingresa el nombre de banda de musica favorita: ")
if (input("¿TIene hijos? S/N"))in ["S","si","s","SI"]:   
    # Solicitar los nombres de los hijos y almacenarlos en una lista
    nombres_hijos = input("Ingresa los nombres de tus hijos separados por comas: ")
    lista_nombres_hijos = nombres_hijos.split(',')
    datos_personales['hijos'] = lista_nombres_hijos
    # Solicitar las fechas de nacimiento de los hijos y almacenarlas en una lista
    fechas_nacimiento_hijos = input("Ingresa las fechas de nacimiento de tus hijos (DD/MM/AAAA) separadas por comas: ")
    lista_fechas_nacimiento_hijos = fechas_nacimiento_hijos.split(',')
    datos_personales['fechas_nacimiento_hijos'] = lista_fechas_nacimiento_hijos



# Guardar los datos en un archivo de texto
nombre_archivo = input("Ingresa el nombre del archivo donde se guardaran los datos: ")
nombre_archivo = nombre_archivo+".txt"
#nombre_archivo = "datos_personales.txt"
with open(nombre_archivo, "w") as archivo:
   # archivo.write("Datos personales:\n")
    for clave, valor in datos_personales.items():
        if clave == 'hijos' or clave == 'fechas_nacimiento_hijos':
            archivo.write(f"{clave}: {', '.join(valor)}\n")
        else:
            archivo.write(f"{clave}: {valor}\n")

print(f"Datos personales guardados en {nombre_archivo}")


def interactive():
    """Implementation of the -i switch. Interactively question the user and
    create a password dictionary file based on the answer."""

    print("\r\n[+] Insert the information about the victim to make a dictionary")
    print("[+] If you don't know all the info, just hit enter when asked! ;)\r\n")

    # We need some information first!

    profile = {}

    name = input("> First Name: ").lower()
    while len(name) == 0 or name == " " or name == "  " or name == "   ":
        print("\r\n[-] You must enter a name at least!")
        name = input("> Name: ").lower()
    profile["name"] = str(name)

    profile["surname"] = input("> Surname: ").lower()
    profile["nick"] = input("> Nickname: ").lower()
    birthdate = input("> Birthdate (DDMMYYYY): ")
    while len(birthdate) != 0 and len(birthdate) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        birthdate = input("> Birthdate (DDMMYYYY): ")
    profile["birthdate"] = str(birthdate)

    print("\r\n")

    profile["wife"] = input("> Partners) name: ").lower()
    profile["wifen"] = input("> Partners) nickname: ").lower()
    wifeb = input("> Partners) birthdate (DDMMYYYY): ")
    while len(wifeb) != 0 and len(wifeb) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        wifeb = input("> Partners birthdate (DDMMYYYY): ")
    profile["wifeb"] = str(wifeb)
    print("\r\n")

    profile["kid"] = input("> Child's name: ").lower()
    profile["kidn"] = input("> Child's nickname: ").lower()
    kidb = input("> Child's birthdate (DDMMYYYY): ")
    while len(kidb) != 0 and len(kidb) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        kidb = input("> Child's birthdate (DDMMYYYY): ")
    profile["kidb"] = str(kidb)
    print("\r\n")

    profile["pet"] = input("> Pet's name: ").lower()
    profile["company"] = input("> Company name: ").lower()
    print("\r\n")

    profile["words"] = [""]
    words1 = input(
        "> Do you want to add some key words about the victim? Y/[N]: "
    ).lower()
    words2 = ""
    if words1 == "y":
        words2 = input(
            "> Please enter the words, separated by comma. [i.e. hacker,juice,black], spaces will be removed: "
        ).replace(" ", "")
    profile["words"] = words2.split(",")

    profile["spechars1"] = input(
        "> Do you want to add special chars at the end of words? Y/[N]: "
    ).lower()

    profile["randnum"] = input(
        "> Do you want to add some random numbers at the end of words? Y/[N]:"
    ).lower()
    profile["leetmode"] = input("> Leet mode? (i.e. leet = 1337) Y/[N]: ").lower()