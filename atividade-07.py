from struct import calcsize


valor = int(input("Digite um valor: "))

calc1 = valor / 3
calc2 = valor / 5

if calc1 or calc2 % 1:
    print(valor," é multiplo de 3 e 5")
else:
    print("falso")