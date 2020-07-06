#estrutura de repetição WHILE
c=1
while c<=10:
    print (c)
    c=c+1
print('Fim!')

n=1
while n!=0:   #condição de parada
    n=int(input('Digite um valor: '))
print ('Fim!')

#DESAFIO 057
sexo=str(input('Qual seu sexo [F/M]? ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo=(str(input('Dados inválidos. Informe seu sexo: [F/M] '))).upper().strip()[0]
print ('Sexo {} registrado com sucesso!'.format(sexo))

#DESAFIO 058
import random
c=random.randint(0,10)
u=int(input('Tente adivinhar o número de 0 a 10 que o computador pensou: '))
while u!=c:
    u=int(input('Você errou. Tente novamente: '))
print('Parabéns, você acertou! O computador também pensou {}.'.format(c))

#DESAFIO 059
import time
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
cmd=0
while cmd!=5:
    time.sleep(1)
    print('''O que você deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior valor\n[4] Digitar novos números\n[5] Sair do programa''')
    cmd=int(input('Sua opção é: '))
    if cmd==1:
        print('A soma é igual a {}.'.format(n1+n2))
    elif cmd==2:
        print('A multiplicação é igual a {}.'.format(n1*n2))
    elif cmd==3:
        print('O maior nº é o {}.'.format(max(n1,n2)))
    elif cmd==4:
        print('Digite novos números:')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif cmd==5:
        print('Finalizando...')
        time.sleep(1)
    else:
        print('Opção inválida. Tente novamente!')
print('Você saiu do programa!')

#DESAFIO 060
#Usando MATH
from math import factorial
x=int(input('Digite um valor inteiro: '))
f=factorial(x)
print('O fatorial de {} é {}.'.format(x,f))

#Usando o WHILE:
n=int(input('Digite um valor inteiro: '))
f=1
while n>0:
    print('{}'.format(n),end='')
    print(' x ' if n>1 else ' = ',end='')
    f*=n  # f=f*n
    n-=1  # n=n-1
print (f)

#DESAFIO 061
print('GERADOR DE PA')
print('-='*10)
n1=int(input('Primeiro termo: '))
r=int(input('Qual a razão? '))
i=1
while i<11:
    print(n1+r,end='')
    print(' > ' if i!=10 else '\nFIM!',end='')
    i+=1
    n1+=r

#DESAFIO 062
print('GERADOR DE PA')
print('-='*10)
n1=int(input('Primeiro termo: '))
r=int(input('Qual a razão? '))
i=1
x=10
t=0
while x!=0:
    t=t+x
    while i<t+1:
        print(n1+r,end='')
        print(' > ' if i!=t else ' PAUSA!',end='')
        i+=1
        n1+=r
    x=int(input('\nQuantos termos você quer mostrar a mais? '))
print ('Progressão finalizada com {} termos mostrados.'.format(t))

#DESAFIO 063
print('SEQUÊNCIA DE FIBONACCI!')
print('-='*12)
n=int(input('Quantos termos você quer mostrar? '))
t=0
t2=1
while t<n:
    print('0 > ')
    t2+=t
    print(t2)