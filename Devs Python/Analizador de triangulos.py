cores = {'limpa':'\033[m',
         'verde':'\033[0;32m',
         'vermelho':'\033[0;31m',
         'fundoverde':'\033[1;40;42m'}

print('{}-=-{}' .format(cores['fundoverde'], cores['limpa']) *10)
print('{}| *Analisador de triângulos* |{}' .format(cores['fundoverde'], cores['limpa']))
print('{}-=-{}' .format(cores['fundoverde'], cores['limpa'])*10)
print('-=-' *20)

#Um dos segmentos tem que ser menor do que a soma do comprimento outros 2.

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM FORMAR{} triângulo!' .format(cores['verde'], cores['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} triângulo!'.format(cores['vermelho'], cores['limpa']))

print('-=-' *20)

