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