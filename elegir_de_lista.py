
import random
from pide_num import pideUnNum 

def elegir_indice(lista: list) -> int:
    ver_lista(lista)
    indice_lista = -1
    while indice_lista not in range(len(lista)):
        print(f"introduce un número del 0 al {len(lista) - 1}")
        indice_lista = pideUnNum()

    return int(indice_lista)

def elegir_varlor(lista: list, indice_lista: int) -> str:
    # valor_lista = lista[elegir_indice(lista)]
    valor_lista = lista[indice_lista]

    return valor_lista

def elegir_valor_azar(lista: list, indice_lista: int) -> str:
    valor_lista_azar = lista[elegir_indice_azar(lista)]

    return valor_lista_azar

def ver_lista(lista: list) -> None:
    indice_pantalla = 0
    for i in lista:
        print(f"{indice_pantalla} - {i}")
        indice_pantalla += 1 

def elemento_lista(lista: list, indice_lista: int) -> None:
    elemento_lista = (f"{lista[indice_lista]} es el elemento {indice_lista}")
    print(elemento_lista)

def elegir_indice_azar(lista: list) -> int:
    indice_aleatorio = random.randrange(len(lista))

    return indice_aleatorio



