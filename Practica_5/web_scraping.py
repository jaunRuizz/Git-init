# Librerias a utilizar
import requests
from bs4 import BeautifulSoup
import os
import time
import argparse
from openpyxl import Workbook
from progress.bar import Bar, ChargingBar
import random


# Tableta de colores para texto
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'


# Funcion que muestra la barra de carga de proceso de lso datos


def barra():
    bar2 = ChargingBar('Obteniendo Datos:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.1))
        bar2.next()
    bar2.finish()

# Funcin para traer las imagenes de celulares de mercado libre


def archivo_img(url_img):
    archivo = open("imagenes.txt", "w")
    for elm in url_img:
        archivo.write(str(elm.get("data-src"))+"\n")
    archivo.close()


# Funcuon para hacer las peticiones al servidor nos traemos el html


def cont(url: str) -> BeautifulSoup:
    respuesta = requests.get(url)
    return BeautifulSoup(respuesta.content, "html.parser")


# Funcion que recibe los argumentos para el funcionamiento del script


def argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="url",
                        help="Ingresa el url de lapagina web: ")
    url = parser.parse_args()
    return url


# Funcion para traernos las imagenes de los
# celulares la primera pagina de mercado libre


def celulares(url):
    if url.url is None:
        print("Error argumento url vacio usa --help para mas ayuda ")
    else:
        contenido = cont(url.url)
        celulares = contenido.find_all("img")

    return celulares


# Funcion que sirve para traernos los datos
# de los celulares modelos y caractweristicas


def items(url):
    if url.url is None:
        print("Error argumento url vacio usa --help para mas ayuda ")
    else:
        contenido = cont(url.url)
        cvss = contenido.find_all("h2")
    return cvss


# Funcion para llenar un archivo excel con los datos de la funcion anterior


def cvs(cvss):
    libro = Workbook()
    pagina = libro.active
    pagina1 = libro.create_sheet("Celulares")
    c = 1
    for elem in cvss:
        pagina1['A'+str(c)] = elem.text
        c = c + 1
    libro.save("Celulares_modelso.xlsx")


print(R+"")
print("  __      __      ___.     _________            .__              ")
print(" /  \    /  \ ____\_ |__  /   _____/ ___________|__|__________   ")
print(" \   \/\/   // __ \| __ \ \_____  \_/ ___\_  __ \  \____ \__  \  ")
print("  \        /\  ___/| \_\ \/        \  \___|  | \/  |  |_> > __ \_")
print("   \__/\  /  \___  >___  /_______  /\___  >__|  |__|   __(____  /")
print("        \/       \/    \/        \/     \/         |__|       \/ ")
print(""+G)      
print(C+"")                                                      
print("[*] Herramienta creada por Luevano Ruiz Juan Daniel ")
print("[*] Gint Hub: https://github.com/jaunRuizz")
print(""+G)

# Le damos jerarquia a las funciones dentro de nuestro script


if __name__ == "__main__":
    url = argumentos()
    url_img = celulares(url)
    archivo_img(url_img)
    cvss = items(url)
    cvs(cvss)
    barra()
    print("Extraccion de datos Finalizada")
    print(""+W)
