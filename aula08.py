# função from/import para importar partes de uma biblioteca
from math import sqrt,floor
n=(int(input('Digite um número: ')))
raiz = sqrt(n)
print('A raiz quadrada de {} arredondada para baixo é igual a {}.'.format(n,floor(raiz)))

#função import para importar uma biblioteca inteira
import math
n=(int(input('Digite um número: ')))
raiz = math.sqrt(n)     #sqrt: raiz quadrada
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n,raiz))
print('Arredondada para cima é igual a {}.'.format(math.ceil(raiz)))   #ceil: arredonda para cima 
print('Arredondada para baixo é igual a {}.'.format(math.floor(raiz)))  #floor arredonda para baixo

# importando bibliotecas externas (PYPI)
#amb virtual: meuenv\Scripts\activate
#pip install emoji --upgrade
import emoji
print(emoji.emojize('Olá, mundo! :earth_americas:',use_aliases=True))

#desafio 016
import math
r=(float(input('Digite um número: ')))
print('O número inteiro é {}.'.format(math.floor(r)))

#desafio 017
import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hip=math.sqrt(math.pow(co,2)+math.pow(ca,2))
print('O comprimento da hipotenusa é {:.2f}'.format(hip))

#desafio 018
ang=float(input('Digite o ângulo: '))
print('Seno = {:.3f}\nCosseno = {:.3f}\nTangente = {:.3f}'.format(math.sin(ang),math.cos(ang),math.tan(ang)))

#desafio 019
import random
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
lista=(a1,a2,a3,a4)
print('O aluno que vai apagar o quadro é {}.'.format(random.choice(lista)))

#desafio 020
import random
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

#desafio 021
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('house_lo.mp3')
pygame.mixer.music.play()
pygame.event.wait()