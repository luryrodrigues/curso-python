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