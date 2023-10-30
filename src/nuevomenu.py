import random
import string

def interactive():
    """Implementation of the -i switch. Interactively question the user and
    create a password dictionary file based on the answer."""

    print("\r\n[+] Introduce informacion sobre la persona para hacer un diccionario de fuerza bruta basado en su perfil")
    print("[+] Si no sabes algun dato, pulsa intro para saltar a la siguiente pregunta.\r\n")

    # We need some information first!

    profile = {}

    nombre = input("> First nombre: ").lower()
    while len(nombre) == 0 or nombre == " " or nombre == "  " or nombre == "   ":
        print("\r\n[-] You must enter a nombre at least!")
        nombre = input("> nombre: ").lower()
    profile["nombre"] = str(nombre)

    profile["apellido"] = input("> apellido: ").lower()
    profile["nick"] = input("> Nick: ").lower()
    fecha_nacimiento = input("> Fecha de Nacimiento (DDMMYYYY): ")
    while len(fecha_nacimiento) != 0 and len(fecha_nacimiento) != 8:
        print("\r\n[-] Debes ingresar 8 dígitos para el cumpleaños.!")
        fecha_nacimiento = input("> Fecha de nacimiento (DDMMYYYY): ")
    profile["fecha_nacimiento"] = str(fecha_nacimiento)

    print("\r\n")

    profile["mujer"] = input("> Conyuge / pareja / novi@ nombre: ").lower()
    profile["mujern"] = input("> Conyuge / pareja / novi@ nickname: ").lower()
    mujerb = input("> Conyuge / pareja / novi@ Fecha de Nacimiento (DDMMYYYY): ")
    while len(mujerb) != 0 and len(mujerb) != 8:
        print("\r\n[-] Debes ingresar 8 dígitos para el cumpleaños.!")
        mujerb = input("> Conyuge / pareja / novi@ Fecha de Nacimiento (DDMMYYYY): ")
    profile["mujerb"] = str(mujerb)
    print("\r\n")

    profile["kid"] = input("> Child's nombre: ").lower()
    profile["kidn"] = input("> Child's nickname: ").lower()
    kidb = input("> Child's fecha_nacimiento (DDMMYYYY): ")
    while len(kidb) != 0 and len(kidb) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        kidb = input("> Child's fecha_nacimiento (DDMMYYYY): ")
    profile["kidb"] = str(kidb)
    print("\r\n")

    profile["pet"] = input("> Pet's nombre: ").lower()
    profile["company"] = input("> Company nombre: ").lower()
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

    print(profile)

def leet_speak_vocals(input_text):
    leet_dict = {
        'A': '4',
        'E': '3',
        'I': '1',
        'O': '0',
    }

    leet_text = "".join(leet_dict.get(c, c) for c in input_text.upper())
    return leet_text

def leet_speak(input_text):
    leet_dict = {
        'A': '4',
        'E': '3',
        'G': '6',
        'I': '1',
        'O': '0',
        'S': '5',
        'T': '7',
    }

    leet_text = "".join(leet_dict.get(c, c) for c in input_text.upper())
    return leet_text

def generate_random_password(length):
    if length < 8:
        print("La longitud de la contraseña debe ser al menos 4 caracteres.")
        return

    num = random.choice(string.digits)
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    punctuation = random.choice(string.punctuation)

    characters = string.digits + string.ascii_letters + string.punctuation
    remaining_length = length - 4

    password = [num, lowercase, uppercase, punctuation]

    for _ in range(remaining_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = ''.join(password)
    return password

def display_banner():
    print("        .. -... .-.. ....- --.. --.- ..- ...-- --..            ")
    print(" ________  ________  ________   ________  ________  ___    ___ ")
    print("|\   __  \|\   __  \|\   ____\ |\   ____\|\   __  \|\  \  /  /| ")
    print("\ \  \|\  \ \  \|\  \ \  \___|_\ \  \___|\ \  \|\  \ \  \/  / |")
    print(" \ \   ____\ \   __  \ \_____  \\ \_____  \ \   ____\ \    / / ")
    print("  \ \  \___|\ \  \ \  \|____|\  \\|____|\  \ \  \___|\/  /  /  ")
    print("   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \__\ __/  / /    ")
    print("    \|__|     \|__|\|__|\_________\\_________\|__||\___/ /     ")
    print("                       \|_________\|_________|    \|___|/    ")
    print("")
    print(" _               ____  _ _     _ _  _                 _____    ")
    print("| |__  _   _    / __ \(_) |__ | | || | ______ _ _   _|___ /____")
    print("| '_ \| | | |  / / _` | | '_ \| | || ||_  / _` | | | | |_ \_  /")
    print("| |_) | |_| | | | (_| | | |_) | |__   _/ / (_| | |_| |___) / / ")
    print("|_.__/ \__, |  \ \__,_|_|_.__/|_|  |_|/___\__, |\__,_|____/___|")
    print("       |___/    \____/                       |_|               ")
    print("")
    print("        .. -... .-.. ....- --.. --.- ..- ...-- --..            ")
    print("\n\n")
def main_menu():
    while True:
        display_banner()
        print("MENU PRINCIPAL: \n")
        print("Seleccione una opcion: \n")
        print("1. Generar contraseña aleatoria")
        print("2. Transformar texto a lenguaje leet")
        print("3. Transformar texto a lenguaje leet solo vocales")
        print("4. Crear Diccionario desde perfil")
        print("\n0. Salir")

        choice = input("\nSeleccione una opción (1/2/3/4): ")

        if choice == "1":
            length = int(input("\nIngrese la longitud de la contraseña: "))
            password = generate_random_password(length)
            print("\nContraseña generada:\t", password)
            input("\nPresione Enter para volver al menú principal.")
        elif choice == "2":
            text = input("\nIngrese el texto a convertir a lenguaje leet: ")
            leet_text = leet_speak(text)
            print("\nTexto en lenguaje leet:\t", leet_text)
            input("\nPresione Enter para volver al menú principal.")
        elif choice == "3":
            text = input("\nIngrese el texto a convertir a lenguaje leet de vocales: ")
            leet_text = leet_speak_vocals(text)
            print("\nTexto en lenguaje leet:\t", leet_text)
            input("\nPresione Enter para volver al menú principal.")
        elif choice == "4":
            interactive()
            input("\nPresione Enter para volver al menú principal.")
        elif choice == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main_menu()


