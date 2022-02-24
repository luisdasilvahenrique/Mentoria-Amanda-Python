lista = []
i = 0
while i != 'parar':
    dado = input('Digite um nome e (stop) para parar: ')
    lista.append(dado)
    i += 1
    if dado == 'stop':
        break

    print(sorted(lista))