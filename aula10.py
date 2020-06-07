#CONDIÇÕES
tempo=int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Carro novo.')
else:
    print('Carro velho')
print('--FIM--')
# if simplificado: print('carro novo' if tempo<=3 else 'carro velho')

#DESAFIO 028
import random
nc=random.randint(0,10)
nu=int(input('Adivinhe que número estou pensando entre 0 e 10: '))
if nc==nu:
    print('Parabéns, eu também pensei no {}.'.format(nc))
else:
    print('Que pena. Eu pensei no {}.'.format(nc))
print('Foi bom brincar com você! Até mais.')

#DESAFIO 029
v=int(input('Qual a velocidade do carro? '))
m=(v-80)*7
if v>80:
    print('Você foi multado. Sua multa é de {} reais.'.format(m))
else:
    print('Parabéns! Você está dentro do limite de segurança.')

#DESAFIO 030
num=int(input('Digite um número inteiro: '))
print('Número par' if num%2==0 else 'Número ímpar')

#DESAFIO 031
d=int(input('Distância da viagem: '))
if d<=200:
    print('A passagem custa {:.2f} reais.'.format(d*0.5))
else:
    print('A passagem custa {:.2f} reais.'.format(d*0.45))

#DESAFIO 032
ano=int(input('Qual é o ano? '))
if ano%4==0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')

#DESAFIO 033
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite outro número: '))
if n1>n2 and n2>n3:
    print('O número {} é o maior e o {} é o menor.'.format(n1,n3))
else:
    if n1>n3 and n3>n2:
        print('O número {} é o maior e o {} é o menor.'.format(n1,n2))
    else:
        if n2>n1 and n1>n3:
            print('O número {} é o maior e o {} é o menor.'.format(n2,n3))
        else:
            if n2>n3 and n3>n1:
                print('O número {} é o maior e o {} é o menor.'.format(n2,n1))
            else:
                if n3>n1 and n1>n2:
                    print('O número {} é o maior e o {} é o menor.'.format(n3,n2))
                else:
                    if  n3>n2 and n2>n1:
                        print('O número {} é o maior e o {} é o menor.'.format(n3,n1))
                    else:
                        print('Há números iguais.')

#DESAFIO 034
s=float(input('Qual é o seu salário? '))
if s>1250.00:
    print('Aumento de 10%. Seu salário será {:.2f}.'.format(s*1.1))
else:
    print('Aumento de 15%. Seu salário será {:.2f}'.format(s*1.15))

#DESAFIO 035
r1=int(input('Primeira reta: '))
r2=int(input('Segunda reta: '))
r3=int(input('Terceira reta: '))
if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')