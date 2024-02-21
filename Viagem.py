v1=float(input("Digite a distância da viagem: "))
print("VocÊ está prestes a começar a sua viagem de {}Km" .format(v1))
if v1>200:
    valor=(v1*0.45)
    print("O valor da sua viagem é de {:.2}" .format(valor))
else:
    valor=v1*0.5
    print("O valor da sua viagem é de {:.2}" .format(valor))