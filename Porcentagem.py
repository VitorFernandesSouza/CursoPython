#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input("Digite o salário do funcionário: "))
if salario>1250:
    NovoSalario=salario+(salario/10)
else:
    NovoSalario=salario+((salario/100)*15)

print("O novo salário do funcionário é R$ {:.2f}" .format(NovoSalario))