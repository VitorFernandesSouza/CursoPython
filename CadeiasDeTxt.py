# REGRAS DE FATIAMENTO
frase="Curso em Vídeo Python"
print(frase)# frase inteira
print(frase[9])# mostra somente o caractere na posição 9
print(frase[9:21:2])# mostra inicio e fim, e pula de 2 em 2
print(frase[:5])# não indica o inicio
print(frase[7:])# não indica o fim

# ANÁLISE DE STRING
print(len(frase))# mostra a quantidade de caracteres
print(frase.count('o')) # conta quantos "o" possuem na cadeia de caracteres
print(frase.find('deo'))# encontra a posição inicial do "deo"
print(frase.replace('Python', 'Android')) # substitui a palavra "Python" por "Android"
print(frase.upper()) # transforma a frase toda em maiúscula
print(frase.lower())# transforma a frase toda em minúscula
print(frase.capitalize())# transforma a primeira letra em maiúscula e as outras em minúscula
print(frase.title())# Análisa quantas palavras existem
print(frase.split())# Divide os espaços e gera uma lista com todas as palavras em um cadeia de caracteres
print('-'.join(frase))#


frase2="   Aprenda Python  "
print(frase2)
print(frase2.strip())# remove espaços inúteis
print(frase2.rstrip())# remove soemente espaços inúteis da direita
print(frase2.lstrip())# remove soemente espaços inúteis da esquerda

print("""Welcome! Are you completely new to programming? Learn about why and how to get started with Python. Fortunately, an experienced programmer in any programming language, whatever it may be, can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!""")