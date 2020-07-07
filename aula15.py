n=s=0
while True:
    n=float(input('Digite um valor: '))
    if n==999:
        break     #Interrompe a função WHILE. Nesse caso não soma o valor 999.
    s+=n
# print('A soma é igual a {}.'.format(s))
print(f'A soma é igual a {s:.2f}.')    #ATUALIZAÇÃO PYTHON - F string

#DESAFIO 066
n=s=c=0
while True:
    n=float(input('Digite um número: [999 para sair]'))
    if n==999:
        break
    s+=n
    c+=1
print(f'Você digitou {c} números e a soma deles é {s}.')

#DESAFIO 067
n=c=m=0
while True:
    n=int(input('Quer ver a tabuada de qual valor? [valor negativo para sair] '))
    if n<0:
        break
    print('-='*10)
    print(f'Tabuada do {n}:')
    while c<10:
        c+=1
        m=c*n
        print(f'{c} X {n} = {m}')
    print('-='*10)
    c=0
print('Você finalizou o programa!')

#DESAFIO 068
import random
s=r=n=0
r2=''
print('-='*15)
print('Vamos jogar PAR ou ÍMPAR!!!')
print('-='*15)
while True:
    j=int(input('Qual número de 0 a 10 você quer jogar? '))
    pi=str(input('Você quer PAR ou ÍMPAR? [P/I] ')).upper().strip()
    c=random.randint(0,10)
    n+=1
    s=c+j
    if s%2==0:
        r2='PAR'
    else:
        r2='ÍMPAR'
    print(f'Você jogou {j} e o computador jogou {c}. Total de {s}. DEU {r2}!!!')
    if r2=='PAR' and pi=='P' or r2=='ÍMPAR' and pi=='I':
        print('Você VENCEU!!!')
    else:
        break
print('-='*25)
print(f'GAME OVER!!! Você venceu um total de {n-1} vezes!')
print('-='*25)

#DESAFIO 069
c=maior18=tothomem=mulhermenor20=0
while True:
    c+=1
    print(f'-----{c}ª PESSOA-----')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    contin=str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()
    if idade > 18:
        maior18+=1
    if sexo=='M':
        tothomem+=1
    if sexo=='F' and idade < 20:
        mulhermenor20+=1
    if contin=='N':
        break
print(f'{maior18} pessoa(s) tem mais de 18 anos.')
print(f'{tothomem} pessoas são homens.')
print(f'{mulhermenor20} mulher(es) tem menos que 20 anos.')

#DESAFIO 070
total=maior1000=menorvalor=qtd=0
barato=''
print('-'*40)
print(' '*10+'LOJA SUPER BARATÃO')
print('-'*40)
while True:
    qtd+=1
    prod=str(input('Nome do Produto: '))
    preço=float(input('R$ '))
    contin=str(input('Deseja cadastrar outro produto? [S/N] ')).strip().upper()
    if contin=='S':
        total+=preço
        if preço > 1000:
            maior1000+=1
        if qtd==1:
            menorvalor=preço
            barato=prod
        if preço<menorvalor:
            menorvalor=preço
            barato=prod
    if contin=='N':
        total+=preço
        maior1000+=1
        barato==barato
        menorvalor==menorvalor
        break
    if contin not in 'SN':
        print('Comando Inválido!!!')
        break
print(f'O total da compra foi de {total:.2f} reais.')
print(f'{maior1000} produto(s) custa(m) mais que 1000 reais.')
print(f'O produto mais barato é o/a {barato} que custa {menorvalor:.2f} reais.')

#DESAFIO 071
ced50=ced20=ced10=ced1=0
print('='*30)
print(' '*10+'BANCO CEV')
print('='*30)
v=int(input('Qual valor você quer sacar? R$ '))
ced50=v//50
print(f'Total de {ced50} cédulas de 50 reais.')
v=v-(ced50*50)
ced20=v//20
print(f'Total de {ced20} cédulas de 20 reais.')
v=v-(ced20*20)
ced10=v//10
print(f'Total de {ced10} cédulas de 10 reais.')
v=v-(ced10*10)
ced1=v
print(f'Total de {ced1} cédulas de 1 real.')
v=v-ced1
print('='*30)
print('Obrigado! Volte sempre ao Banco CEV!')