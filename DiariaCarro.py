valorFixo=60

kmPercorrido=float(input("Quantos km foram percorridos? "))
dias=int(input("Por quantos dias o carro foi alugado? "))

adicionalPorKm=kmPercorrido*0.15
diaria=valorFixo*dias

print("O preço final a pagar pelo carro é de: {:.2f} " .format(diaria+adicionalPorKm))
