# função is retorna informações sobre a variável
x=input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(x))
print('Só tem espaços? ',x.isspace())
print('É um número? ',x.isnumeric())
print('É alfabético? ',x.isalpha())
print('É alfanumérico? ',x.isalnum())
print('Está em letras minúsculas? ',x.islower())
print('Está capitalizada? ',x.istitle())