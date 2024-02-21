a=float(input("Valor 1: "))
b=float(input("Valor 2: "))
c=float(input("Valor 3: "))

menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print("O menor número é {} e o maior número é {}" .format(menor, maior))
