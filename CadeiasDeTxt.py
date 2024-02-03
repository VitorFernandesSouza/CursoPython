# REGRAS DE FATIAMENTO
frase="Curso em Vídeo Python"
print(frase)# frase inteira
print(frase[9])# mostra somente o caractere na posição 9
print(frase[9:21:2])# mostra inicio e fim, e pula de 2 em 2
print(frase[:5])# não indica o inicio
print(frase[7:])# não indica o fim

# ANÁLISE DE STRING
print(len(frase))# #Lê a quantidade de posições
print(frase.count('o')) # conta quantos "o" possuem na cadeia de caracteres
print(frase.find('deo'))# encontra a posição inicial do "deo"
print(frase.replace('Python', 'Android')) # substitui a palavra "Python" por "Android"
print(frase.upper()) # transforma a frase toda em maiúscula
print(frase.lower())# transforma a frase toda em minúscula
print(frase.capitalize())# transforma a primeira letra em maiúscula e as outras em minúscula
print(frase.title())# Análisa quantas palavras existem
print(frase.split())# Divide os espaços e gera uma lista com todas as palavras em um cadeia de caracteres
print('-'.join(frase))# Juntas os espaços e gera uma lista com todas as palavras em um cadeia de caracteres



frase2="   Aprenda Python  "
print(frase2)
print(frase2.strip())# remove espaços inúteis
print(frase2.rstrip())# remove somente espaços inúteis da direita
print(frase2.lstrip())# remove soemente espaços inúteis da esquerda

print("""Welcome! Are you completely new to programming? Learn about why and how to get started with Python. Fortunately, an experienced programmer in any programming language, whatever it may be, can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!""")

#Nome com todas as letras maiúsculas
nome=input("Escreva seu nome: ")
print("O seu nome escrito com todas as letras maiúsculas é: "+ nome.upper())

#Nome com todas a letras minúsculas
print("O seu nome escrito com todas as letras minúsculas é: "+ nome.lower())

#Quantas letras tem o nome sem contar os espaços
print("O seu nome tem {} letras" .format(len(nome.replace(' ', ''))))

#Quantas letras tem o primeiro nome
nome1=nome.split()
print("A quantidade de letras do seu primeiro nome é: {}" .format(len(nome1[0])))


#Soluções do professor
print("O seu nome escrito com todas as letras maiúsculas é {} ".format(nome.upper()))
print("O seu nome escrito com todas as letras minúsculas é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras" .format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Devolvendo True or False para uma palavra chave
cidade=input("Qual a cidade que vc nasceu? ").strip()
print(cidade[:5].upper() == 'SANTO')


#Crie um programa que leia o nome de uma pessoa e diga se ela tem “FERNANDES” no nome.
nome=input("Digite o seu nome: ").strip()
print("O seu nome tem Fernandes? {}" .format('FERNANDES' in nome.upper())) #Operador "in", usado para verificar a existência de um valor em uma lista

#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase=input("Digite uma frase: ").strip() .upper()
print("A letra 'A' aparece {} na frase" .format(frase.count('A')))
print("O primeiro A fica na posição {}".format(frase.find('A')+1))
print("A última letra A pareceu na posição {}" .format(frase.rfind('A')+1)) #rfind (comece a procurar pela direita)

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name=input("Digite seu nome completo: ")
name1=name.split()
print("O seu primeiro nome é {}" .format(name1[0]))
print("O seu último nome é {}" .format(name1[len(name1)-1])) #len --> lê a quantidade de posições --> -1 pq contamos o 0