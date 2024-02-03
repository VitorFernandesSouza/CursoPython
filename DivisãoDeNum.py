# Programa que lê as unidades, dezenas, centenas e milhares de um número

num=int(input("Escreva um número: "))
u= num // 1 %10
d= num // 10 %10
c= num // 100 %10
m= num // 1000 %10
print("Unidades: {}" .format(u))
print("Dezenas: {}".format(d))
print("Centenass: {}".format(c))
print("Milhar: {}".format(m))

