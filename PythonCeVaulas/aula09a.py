## MANIPULANDO STRINGS ##

frase = 'Curso em Video Python'

## FATIAMENTO ##

# Letra da posição 9 #
frase[9]

# Letras da posição 9 até 13 #
frase[9:14]

# Letras da posição 15 até última #
frase[15:]

# Letras da posição 9 até a última, pulando de 2 em 2 #
frase[9::2]

# Letras da posição inicial até a 5 #
frase[:5]

## ANÁLISE ##

# Tamanho da frase #
len(frase)

# Quantas letras 'o' tem na frase #
frase.count('o')

# Conta 'o' da posição 0 até a 12 #
frase.count('o' ,0 ,13 )

# Encontra onde está o 'deo' na frase #

frase.find('deo')

# Encontra onde está o 'Android' na frase (erro retorna -1) #

frase.find('Android')

# Confere se a palavra 'Curso' está na frase e me retorna verdadeiro ou falso #

print('Curso' in frase)

## TRANSFORMAÇÃO ##

# Substitui a palavra 'Python' para 'Android' #

frase.replace('Python', 'Android')

# Deixa todas as letras maiúsculas #
frase.upper()

# Deixa todas as letras minúsculas #
frase.lower()

# Deixa apenas a primeira letra maiúscula #
frase.capitalize()

# Deixa todas as palavras com a primeira letra maiúscula #
frase.title()

# Remove espaços inúteis no começo e no final da frase #
frase.strip()

# Remove espaços inúteis no final da frase #
frase.rstrip()

# Remove espaços inúteis no começo da frase #
frase.lstrip()

# Remove todos os espaços entre as palavras e junta tudo #
frase.replace(' ', '')

# Divide a frase em uma lista para cada palavra #
frase.split()

nova_frase = frase.split()

# Mostra a primeira palavra da nova frase #
print(frase.split()[0])

# Mostra a última palavra da nova frase #
print(frase.split()[-1])

print(len(frase.replace(' ', '')))