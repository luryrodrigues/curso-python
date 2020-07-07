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