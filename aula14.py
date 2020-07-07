#estrutura de repetição WHILE
c=1
while c<=10:
    print (c)
    c=c+1
print('Fim!')

n=1
while n!=0:   #condição de parada
    n=int(input('Digite um valor: [0 para parar]'))
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
    if i!=10:
        print(' > ',end='')
    i+=1
    n1+=r
print (' FIM!')

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
n=n-2
c=0
t1=0
t2=1
t3=0
print('0 > 1 > ',end='')
while c<n:
    c+=1
    t3=t1+t2
    t1=t2
    t2=t3
    print(t3,end='')
    if c!=n:
        print(' > ',end='')
print(' FIM!')

#DESAFIO 064
n=int(input('Digite número [999 para parar]: '))
soma=0
cont=1
while n!=999:
    soma+=n
    cont+=1
    n=int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles foi {}.'.format(cont-1,soma))

#DESAFIO 065
cont=soma=med=n=maior=menor=0    # mesma coisa que declarar cada variável em uma linha, coloca assim para deixar o código menor
p='Ss'
while p in 'Ss':
    n=int(input('Digite número: '))
    cont+=1
    soma+=n
    med=soma/(cont)
    if cont==1:
        maior=menor=n
    else:
        if n > maior:
            maior=n
        if n < menor:
            menor=n
    p=str(input('Deseja continuar? [S/N] ')).upper().strip()
if p in 'Nn':
    print('Você digitou {} números e a média deles foi {:.1f}.'.format(cont,med))
    print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))
elif p not in 'SsNn':
    print('Comando inválido!!!')