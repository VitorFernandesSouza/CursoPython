 # Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1=float(input("Segmento 1: "))
r2=float(input("Segmento 2: "))
r3=float(input("Segmento 3: "))

triangulo=r1 < r2+r3 and r2< r1+r3 and r3< r2+r1
if triangulo:
    print("É possível fazer o triângulo com esses segmentos")
else:
    print("NÃO é possível criar um triângulo com esses segmentos")