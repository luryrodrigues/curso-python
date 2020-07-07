#LAÇOS DE REPETIÇÃO
for c in range (1,6):    #python não considera o último nº. Vai contar de 1 a 5 nesse caso
    print(c)
print('Ordem inversa:')
for c in range (5,0,-1):  #o -1 é faz 6-1, 5-1, 4-1 (contagem inversa) 
    print(c)
print('Pulando de 2 em 2:')
for c in range (1,6,2):   # o 2 significa: pular de 2 em 2
    print(c)

s=0
for c in range (0,4):
    n=int(input('Digite um número inteiro: '))
    s+=n                   #s+=n é o mesmo que s= s + n
print('A soma dos valores é {}.'.format(s))

#DESAFIO 046
from time import sleep
import emoji
print('CONTAGEM REGRESIVA!!!')
for c in range (10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:', use_aliases=True))

#DESAFIO 047
print('Números pares de 1 a 50:')
for c in range (2,51,2):
    print(c, end=' ')

#DESAFIO 048
s=0
cont=0
for c in range (1,501,2):
    if c%3==0:
        cont=cont+1  #números de valores retornados
        s+=c
print('A soma de todos os {} valores pares múltiplos de 3 é {}.'.format(cont,s))

#DESAFIO 049
n=(int(input('Digite um número para ver sua tabuada: ')))
print('-'*12)
for c in range(1,11):
    print('{} x {:>2} = {:<2}'.format(n,c,n*c))
print('-'*12)

#DESAFIO 050
s=0
for c in range(1,5):
    num=int(input('Digite um número inteiro: '))
    if num%2==0:
        s+=num
print('A soma dos números pares é {}.'.format(s))

#DESAFIO 051
t1=int(input('Qual o primeiro termo da PA? '))
r=int(input('Qual a razão da PA? '))
for c in range (1,11):
    print(t1+(c*r),end=' -> ')
print('FIM!')

#DESAFIO 052
cont=0
n=int(input('Digite um número inteiro: '))
for c in range(1,n+1):
    if n%c==0:
        cont+=1
if cont>2:
    print('O número digitado não é primo.')
else:
    print('O número digitado é primo.')

#DESAFIO 053
f=str(input('Digite uma frase: ')).upper().strip()
palavras=f.split()
junto=''.join(palavras)
inversa=''    # inversa=junto[::-1] também funciona e nao precisa do for
for letra in range (len(junto)-1,-1,-1):
    inversa+=junto[letra]
print('A frase {} inversa é {}.'.format(junto,inversa))
if junto==inversa:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')

#DESAFIO 054
from datetime import date
contmaior=0
contmenor=0
for c in range (1,6):
    ano=int(input('Ano de nascimento da pessoa {}: '.format(c)))
    if date.today().year-ano >=18:
        contmaior+=1
    else:
        contmenor+=1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(contmaior,contmenor))

#DESAFIO 055
maior=0
menor=0
for p in range(1,6):
    peso=float(input('Peso da pessoa {}: '.format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('A pessoa mais pesada tem {} kg e a mais leve tem {} kg.'.format(maior,menor))

#DESAFIO 056
somaidade=mediaidade=maioridadehomem=totmulher20=0
nomevelho=''
for p in range(1,4):
    print('-----{}ª PESSOA-----'.format(p))
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    somaidade+=idade
    if p==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff'and idade<20:
        totmulher20+=1
mediaidade=somaidade/3
print('A média de idade do grupo é {:.0f}.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('{} mulher(es) tem menos que 20 anos.'.format(totmulher20))
