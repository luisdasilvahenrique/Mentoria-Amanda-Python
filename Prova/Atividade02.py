import math 

print("Bem vindo ao nosso segundo programa em Python \n")

# Y = ax² + bx + c

a = float(input("Digite o primeiro coeficiente da sua equação: "))

b = float(input("Digite o segundo coeficiente da sua equação: "))

c = float(input("Digite o terceiro coeficiente da sua equação: "))

raiz1 =  ((-b + math.sqrt(b*b - 4*a*c))/2*a)
raiz2 =  ((-b - math.sqrt(b*b - 4*a*c))/2*a)

print("\n As raízes são %.2f e %.2f"%(raiz1, raiz2))

# Essa questão é preciso que teste com um valor Negativo para não dar erro de math d1
