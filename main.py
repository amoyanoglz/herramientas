import pide_num
import elegir_de_lista
from lista import lista_elementos

def main():
    lista = lista_elementos[1]
    indice = elegir_de_lista.elegir_indice(lista)
    print("##### el usuario ha elegido ####")
    elegir_de_lista.elemento_lista(lista, indice)
    print()
    print("##### el aleatorio ha elegido ####")
    elegir_de_lista.elemento_lista(lista, elegir_de_lista.elegir_indice_azar(lista))

main()
