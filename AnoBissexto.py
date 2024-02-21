from datetime import date
A1=int(input("Qual ano você quer analisar? "))
bissexto= A1%4 == 0 and A1 %100 != 0 or A1 %400 == 0
if A1 ==0:
    A1= date.today().year
if bissexto:
    print("O ano de {} é bissexto!" .format(A1))
else:
    print("O ano de {} NÃO é bissexto" .format(A1))