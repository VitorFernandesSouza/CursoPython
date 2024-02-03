import math
import os

catetoOposto= float(input("Digite o valor do cateto oposto: "))
catetoAdjacente=float(input("Digite o valor do cateto adjacente: "))

hipotenusa=(catetoOposto**2)+(catetoAdjacente**2)

print("O valor da hipotenusa é igual a: {:.2f}".format(math.sqrt(hipotenusa)))
os.system("cls")


