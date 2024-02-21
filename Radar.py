v1=float(input("Escreva a velocidade do carro: "))
if v1>80:
    valorMulta=(v1-80)*7
    print("Você foi multado! O valor da multa a pagar é de  {:.2f}" .format(valorMulta))
else:
    print("Você está dentro do limite de velocidade permitido")