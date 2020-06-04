# alinhamentos
nome=input('Qual é seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))    # escreve em 20 espaços (pode ser utilizado para casas decimais)
print('Prazer em te conhecer, {:>20}!'.format(nome))   # alinhado a direita em 20 espaços
print('Prazer em te conhecer, {:<20}!'.format(nome))   # alinhado a esqueda em 20 espaços
print('Prazer em te conhecer, {:^20}!'.format(nome))   # centralizado
print('Prazer em te conhecer, {:=^20}!'.format(nome))  # centralizado com caracteres ao invês de espaço vazio

# operadores aritméticos
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2 # divisão inteira
ds=n1%n2  #sobra da divisão inteira
e=n1**n2  #potência
print('A soma vale {},\na multiplicação é {}, a divisão é {:.3f}.'.format(s,m,d))  #.3f: 3 casas flutuantes (decimais), \n : quebra de linha
print('A divisão inteira é {}, a sobra é {}'.format(di,ds), end=' ')  # end: faz com que a linha não quebre
print ('e a potência é {}.'.format(e))

# desafio 005
n=int(input('Digite um número: '))
a=n-1
s=n+1
print('O antecessor de {} é {} e seu sucessor é {}.'.format(n,a,s))

# desafio 006
n=int(input('Digite um número: '))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.3f}.'.format(n,d,t,r))

#desafio 007
n1=int(input('Qual é a nota da P1? '))
n2=int(input('Qual é a nota da P2? '))
m=(n1+n2)/2
print('A nota média do aluno é {:.1f}.'.format(m))

# desafio 008
m=float(input('Digite o comprimento em metros: '))
c=m*100
mm=m*1000
print('{} metros são {} centímetros e {} milímetros.'.format(m,c,mm))

# desafio 009
n=(int(input('Digite um número para ver sua tabuada: ')))
print('-'*12)
print('{} x {:>2} = {:<2}'.format(n,1,n*1))
print('{} x {:>2} = {:<2}'.format(n,2,n*2))
print('{} x {:>2} = {:<2}'.format(n,3,n*3))
print('{} x {:>2} = {:<2}'.format(n,4,n*4))
print('{} x {:>2} = {:<2}'.format(n,5,n*5))
print('{} x {:>2} = {:<2}'.format(n,6,n*6))
print('{} x {:>2} = {:<2}'.format(n,7,n*7))
print('{} x {:>2} = {:<2}'.format(n,8,n*8))
print('{} x {:>2} = {:<2}'.format(n,9,n*9))
print('{} x {:>2} = {:<2}'.format(n,10,n*10))
print('-'*12)

#desafio 010
din=float(input('Quantos reais você tem na sua carteira? '))
print('Você pode comprar {:.2f} dólares.'.format(din/3.27))

#desafio 011
lar=float(input('Qual a largura da parede? '))
h=float(input('Qual a altura da parede? '))
a=lar*h
lit=a/2
print('A parede tem {} metros quadrados e precisa-se de {} litros de tinta para pintá-la.'.format(a,lit))

# desafio 012
sal=float(input('Qual é o seu salário? '))
print('Seu salário com um aumento de 15% é igual a {:.2f}.'.format(sal*1.15))