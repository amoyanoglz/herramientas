def pideUnNum():
    msg = "Dame un numero: "
    entrada = ''
    invalido = False
    while not entrada.isnumeric():
        if invalido:
            print("Obligatoriamente debe ser un número")
        invalido = True
        entrada = input(msg)


    return int(entrada)
