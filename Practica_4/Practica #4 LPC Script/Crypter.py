# Autores Luevano Ruiz and Jose Hernandez
# Librerias importadas
import base64
from typing import Callable

# Tableta de colores para texto
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

# Funcion que conbierte a bytes un mensaje


def codificar_b(
    byte_message: bytes, encode_fn: Callable[[bytes], bytes]
) -> bytes:
    return encode_fn(byte_message)

# Funcion que codifica un texto en Ascii


def codificar_texto(text: str, encoding_format: str = "ascii") -> str:
    return codificar_b(text.encode(encoding_format), base64.b64encode).decode(
        encoding_format
    )

# Funcion para decodificar un texto en Ascii


def decodificar_texto(text: str, encoding_format: str = "ascii") -> str:
    return codificar_b(text.encode(encoding_format), base64.b64decode).decode(
        encoding_format
    )

# Funcion para codificar un archivo


def codificar_archivo(path: str) -> bytes:
    with open(path, "rb") as file_to_encode:
        return codificar_b(file_to_encode.read(), base64.b64encode)

# Funcion para decodificar un archivo


def decodificar_archivo(path: str) -> bytes:
    file_to_encode = open(path, "rb")
    return codificar_b(file_to_encode.read(), base64.b64decode)

# Funcion que sirve para guardar el contenido
# de la codificacion o la decodificacion


def guardar(path: str, content: bytes) -> None:
    with open(path, "wb") as file_to_save:
        file_to_save.write(content)


def encode_plus_one(word: str) -> str:
    return "".join([chr(ord(character) + 2) for character in word])


# Menu de opciones para el script


def menu():
    print(C+"                         ")
    print("[1] Codificar texto        ")
    print("[2] Decodificar texto      ")
    print("[3] codificar un archivo   ")
    print("[4] decodificar un archivo ")
    print("[0] Para salir           "+W)

# Submenu #1


def codificar_t():
    texto = input("ingresa el texto a codificar: ")
    mensaje = codificar_texto("{}".format(texto))
    print("El mensaje codificado es: ", mensaje)
    archivo = open("Texto.txt", "w")
    archivo.write(str(mensaje))
    archivo.close()
    print("Se creo archivode texto con el mensaje encriptado")
# Submenu #2


def decodificar_t():
    texto_decodificar = input("Ingresa el texto que deceas decodificar: ")
    mensaje = decodificar_texto("{}".format(texto_decodificar))
    print("El mensaje decodificado es: ", mensaje)
    archivo = open("Texto_decodificado.txt", "w")
    archivo.write(str(mensaje))
    archivo.close()
    print("Se creo archivo de texto con el mensaje decodificado")
# Submenu #3


def codificar_a():
    name_archivo = input("ingresa el nombre del archivo: ")
    guardar("texto_codificada.txt",
            codificar_archivo("{}".format(name_archivo)))
    op = input("Deseas codificar otro archivo si/[y] no/[n] ->")
    count = 2
    while op == "y":
        name_archivo = input("ingresa el nombre del archivo: ")
        guardar("texto_codificada"+str(count)+".txt",
                codificar_archivo("{}".format(name_archivo)))
        count = count + 1
        op = input("Deseas codificar otro archivo si/[y] no/[n] -> ")
    else:
        exit()
# Submenu #4


def decodificar_a():
    name_archivo = input("ingresa el nombre del archivo: ")
    guardar("img_decodificada.jpg",
            decodificar_archivo("{}".format(name_archivo)))
    op = input("Deseas decodificar otro archivo si/[y] no/[n] ->")
    count = 2
    while op == "y":
        name_archivo = input("ingresa el nombre del archivo: ")
        guardar("img_decodificada"+str(count)+".jpg",
                decodificar_archivo("{}".format(name_archivo)))
        count = count + 1
        op = input("Deseas decodificar otro archivo si/[y] no/[n] -> ")
    else:
        exit()
# Name del programa
print(G+"                                                      ")
print("   _________                        __                  ")
print("   \_   ___ \_______ ___.__._______/  |_  ___________   ")
print("   /    \  \/\_  __ <   |  |\____ \   __\/ __ \_  __ \  ")
print("   \     \____|  | \/\___  ||  |_> >  | \  ___/|  | \/  ")
print("    \______  /|__|   / ____||   __/|__|  \___  >__|     ")
print("           \/        \/     |__|             \/         ")
print("                                                      "+W)

# Informacion de contacto y creadores del script
print(R+"")
print("*************************************************" +
      "**************************************" +
      "**********************************")
print("*        [inf] Este script Fue creado por Juan Da" +
      "niel Luevano Ruiz En colaboracion" +
      "con JOSE ANASTACIO HERNANDEZ SALDAÑA *")
print("*        Repo] --> https://github.com/jaunRuizz/G"
      "it-init.git *")
print("*        Recuerda que los archivos los tienes que" +
      "guardar en la carpeta donde clonaste tu repo *")
print("**************************************************" +
      "**********************************************" +
      "*************************")
print(""+W)

# Funcion que ejecuta el script con el menu


def default():
    menu()
    op = int(input("Elije una opcion: "))
    while op == 1 or op == 2 or op == 3 or op == 4:
        if op == 1:
            codificar_t()
        elif op == 2:
            decodificar_t()
        elif op == 3:
            codificar_a()
        elif op == 4:
            decodificar_a()
        menu()
        op = int(input("Elije una opcion: "))
    else:
        exit()

# Ejecucion del programa
if __name__ == "__main__":
    default()
