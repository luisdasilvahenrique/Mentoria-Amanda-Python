listaNum = []
mai = 0
men = 0
for c in range(0, 50): #Aqui você pode determinar quantos valores você quer ler 1° parametro de onde quer começar e o 2° quantas vezes quer repetir.
    listaNum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listaNum[c]
    else:
        if listaNum[c] > mai:
            mai = listaNum[c]
        if listaNum[c] < men:
            men = listaNum[c]
print(f'O maior valor digitado foi: {mai}')
print(f'O menor valor digitado foi: {men}')