# FATIAMENTO
frase= 'Curso em vídeo Python'
print(frase[9])
print(frase[9:14])  #caracter 9 até o 13
print(frase[9:14:2]) #caracter 9 ao 14 pulando de 2 em 2
print(frase[:5])  #começo até o caracter 5
print(frase[15:]) #caracter 15 até o final
print(frase[9::3])  #caracter 9 até o final pulando de 3 em 3

#ANÁLISE DE STRING
print(len(frase))   #comprimento da frase
print(frase.count('o'))  #conta o numero de caracteres 'o'
print(frase.count('o',0,13))  #conta o numero de caracteres 'o' do 0 ao 12
print(frase.find('deo'))  #encontra string e retorna onde ela começa
print(frase.find('android'))  #retorna valor -1 porque a string nao foi encontrada
print('Curso' in frase)    #Existe a palavra Curso na frase? True or False

#TRANSFORMAÇÃO
print(frase.replace('Python','Android'))   #substituir palavras
print(frase.upper())  #letras maiúsculas
print(frase.lower())  #letras minusculas
print(frase.capitalize())  #primeiro caracter em maiusculo
print(frase.title())   #todas as palavras em maiusculo
frase2='    Aprenda Python    '
print(frase2.strip())   #retira espaços do começo e do 
print(frase2.rstrip())  #retira apenas os espaçoes da direita
print(frase2.lstrip())  #retira apenas os espaços da esquerda

#DIVISÃO
print(frase.split())  #a contagem de caracter é feita palavra a palavra e nao da frase toda. Separa em listas
dividido=frase.split()
print('-'.join(dividido))   #junta as palavras com o separador -
print(dividido[2][3])  #mostra o caracter 3 da segunda lista

#DESAFIO 022
nome=str(input('Qual seu nome completo? '))
print(nome.upper())
print(nome.lower())
dividido=nome.split()
semesp=(''.join(dividido))
print('Seu nome tem {} letras.'.format(len(semesp)))
print('O primeiro nome tem {} letras.'.format(len(dividido[1])))