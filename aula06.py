# a função input gera uma variável
nome=input('Qual é o seu nome? ')
idade=input('Qual a sua idade? ')
peso=input('Quanto você pesa? ')
print(nome,idade,peso)

#inserindo uma variável na função print
nome=input('Qual seu nome? ')
print('Olá,',nome,'! Seja bem vindo(a)!')
print('Olá, {}! Seja bem-vindo(a)!'.format(nome))

# classificando variáveis: int, float, bool ou str. Aqui, se a variável não for classificada, não é feita a soma
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma é igual a : ',s)

#DISSECANDO UMA VARIÁVEL
# função is retorna informações sobre a variável
x=input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(x))
print('Só tem espaços? ',x.isspace())
print('É um número? ',x.isnumeric())
print('É alfabético? ',x.isalpha())
print('É alfanumérico? ',x.isalnum())
print('Está em letras minúsculas? ',x.islower())
print('Está capitalizada? ',x.istitle())