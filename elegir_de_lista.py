
import random
from pide_num import pideUnNum 


def elegir_indice(lista):
    ver_lista(lista)
    indice_lista = -1
    while indice_lista not in range(len(lista)):
        print(f"introduce un número del 0 al {len(lista) - 1}")
        indice_lista = pideUnNum()

    return int(indice_lista)

def ver_lista(lista):
    indice_pantalla = 0
    for i in lista:
        print(f"{indice_pantalla} - {i}")
        indice_pantalla += 1 

def elemento_lista(lista, indice_lista):
    elemento_lista = (f"{lista[indice_lista]} es el elemento {indice_lista}")
    print(elemento_lista)

    # return elemento_lista


def elegir_aleatorio(lista):
    indice_aleatorio = random.randrange(len(lista))

    return indice_aleatorio
