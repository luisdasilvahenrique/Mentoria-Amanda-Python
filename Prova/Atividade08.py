listaOne = []
listaTwo = []
cont = 0
while True:
    dataOne = input('Digite alguma coisa na lista 1, para encerrar[stop]: ')
    listaOne.append(dataOne)

    dataTwo = input('Digite alguma coisa na lista 2, para encerrar[stop]: ')
    listaTwo.append(dataTwo)

    if dataOne == "stop":
        break
    elif dataTwo == "stop":
        break

    cont += 1

    if listaOne == listaTwo:
        print(
            f'Verdadeiro, as listas são iguais! \nOs dados são {listaOne} e {listaTwo}.')
    else:
        print(
            f'Falso, as listas são diferentes! \nOs dados são {listaOne} e {listaTwo}.')
