#CONDIÇÕES ANINHADAS
nome=str(input('Qual seu nome? '))
if nome=='Lury':
    print('Que nome lindo!')
elif nome=='Maria' or nome=='João':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Julia Valentina Isadora':
    print('Belo nome feminino!')
else:                                  #o else é opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#DESAFIO 036
v=float(input('Qual o valor da casa? R$ '))
s=float(input('Qual seu salário? R$ '))
a=int(input('Em quantos anos você vai pagar? '))
p=v/(a*12)
if p>(0.3*s):
    print('Empréstimo negado!')
else:
    print ('Empréstimo aprovado!')

#DESAFIO 037
n=int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')        #3 aspas para quebrar as linhas do texto
opcao=int(input('Sua opção: '))
if opcao==1:
    print('{} convertido para binário é {}.'.format(n,bin(n)[2:]))     #[2:] para começar a contar a partir do 3º nº
elif opcao==2:
    print('{} convertido para octal é {}.'.format(n,oct(n)[2:]))
elif opcao==3:
    print('{} convertido para hexadecimal é {}.'.format(n,hex(n)[2:]))
else:
    print('Opção inválida.')

#DESAFIO 038
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
if n1>n2:
    print('{} é maior.'.format(n1))
elif n2>n1:
    print('{} é maior'.format(n2))
else:
    print('Os números são iguais.')

#DESAFIO 039
from datetime import date
ano=int(input('Qual o ano do seu nascimento? '))
atual=date.today().year       # retorna o ano da data de hoje
if (atual-ano)<18:
    print('Faltam {} anos para se alistar ao serviço militar.'.format(18-(atual-ano)))
elif (atual-ano)==18:
    print('Você tem 18 anos. Hora de se alistar ao serviço militar.')
else:
    print('Já passaram {} anos do alistamento ao serviço militar.'.format((atual-ano)-18))

#DESAFIO 040
n1=float(input('Nota da P1: '))
n2=float(input('Nota da P2: '))
m=(n1+n2)/2
if m<5.0:
    print('Sua média é {:.1f}. \033[31mREPROVADO\033[m!'.format(m))
elif m>=5 and m<=6.9:
    print('Sua média é {:.1f}. \033[33mRECUPERAÇÃO\033[m!'.format(m))
else:
    print('Sua média é {:.1f}. \033[32mAPROVADO\033[m!'.format(m))

#DESAFIO 041
from datetime import date
nasc=int(input('Qual seu ano de nascimento? '))
i=(date.today().year)-nasc
if i<=9:
    print('Sua idade é {}. Você é um atleta mirim.'.format(i))
elif 9<i<=14:
    print('Sua idade é {}. Você é um atleta infantil.'.format(i))
elif 14<i<=19:
    print('Sua idade é {}. Você é um atleta junior.'.format(i))
elif 19<i<=20:
    print('Sua idade é {}. Você é um atleta senior.'.format(i))
else:
    print('Sua idade é {}. Você é um atleta master.'.format(i))

#DESAFIO 42
r1=int(input('Primeira reta: '))
r2=int(input('Segunda reta: '))
r3=int(input('Terceira reta: '))
if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    if r1==r2==r3:
        print('As retas formam um triângulo EQUILÁTERO.')
    elif r1!=r2!=r3:   #!= significa diferente
        print('As retas formam um triângulo ESCALENO.')
    else:
        print('As retas formam um triângulo ISÓSCELES.')
else:
    print('As retas não formam um triângulo.')

#DESAFIO 43
p=float(input('Qual seu peso? (Kg) '))
h=float(input('Qual sua altura? (m) '))
imc=p/h**2
if imc < 18.5:
    print('IMC = {:.1f}. Abaixo do peso'.format(imc))
elif  imc <= 25:
    print('IMC = {:.1f}. Peso ideal'.format(imc))
elif imc <= 30:
    print('IMC = {:.1f}. Sobrepeso'.format(imc))
elif imc <= 40:
    print('IMC = {:.1f}. Obesidade'.format(imc))
else:
    print('IMC = {:.1f}. Obesidade mórbida'.format(imc))

#DESAFIO 044
p=float(input('Preço total das compras: R$ '))
pg=int(input('''Selecione a forma de pagamento:
[1] à vista dinheiro
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão
Sua opção é: '''))
if pg==1:
    print('Desconto de 10%. Preço final: R$ {:.2f}'.format(p*0.9))
elif pg==2:
    print('Desconto de 5%. Preço final: R$ {:.2f}'.format(p*0.95))
elif pg==3:
    print('Sem desconto. Preço final: R$ {:.2f}'.format(p))
elif pg==4:
    print('Juros de 20%. Preço final: R$ {:.2f}'.format(p*1.2))
else:
    print('Opção de pagamento inválida.')

#DESAFIO 045 - JOKENPÔ
import random
from time import sleep
itens=('PEDRA','PAPEL','TESOURA')
c=random.randint(0,2)
print('''Jogue uma das opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j=int(input('Sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*20)
sleep(1)
print('O computador escolheu {}.'.format(itens[c]))
sleep(1)
print('O jogador escolheu {}.'.format(itens[j]))
sleep(1)
print('-='*20)
sleep(1)
if c==j:
    print('EMPATE!!!')
elif c==0 and j==1:
    print('Jogador venceu!')
elif c==0 and j==2:
    print('Computador venceu!')
elif c==1 and j==0:
    print('Computador venceu!')
elif c==1 and j==2:
    print('Jogador venceu!')
elif c==2 and j==0:
    print('Jogador venceu!')
elif c==2 and j==1:
    print('Computador venceu!')
else:
    print('Opção inválida. Jogue novamente!')