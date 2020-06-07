#CORES NO TERMINAL
print('\033[1;31;43mOlá, mundo!\033[m')   #nº entre colchete: style, txt, back - Verificar padrão ANSI

#FORMA 1
print ('O semáforo significa \033[31mPare\033[m, \033[33mAtenção\033[m e \033[32mSiga\033[m.')

#FORMA 2
print('O semáforo significa {}Pare{}, {}Atenção{} e {}Siga{}.'.format('\033[31m','\033[m','\033[33m','\033[m','\033[32m','\033[m'))

#LISTA DE CORES - FORMA 3
cores={'limpa':'\033[m','vermelho':'\033[31m','amarelo':'\033[33m','verde':'\033[32m'}
print('O semáforo significa {}Pare{}, {}Atenção{} e {}Siga{}.'.format(cores['vermelho'],cores['limpa'],
cores['amarelo'],cores['limpa'],cores['verde'],cores['limpa']))