cores = {'limpa':'\033[m',
         'verde':'\033[0;32m',
         'vermelho':'\033[0;31m',
         'fundoverde':'\033[1;40;42m'}

print('-=-' *20)

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
#verificando quem é menor:
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O {}menor{} valor foi {}.' .format(cores['verde'], cores['limpa'], menor))

#verificando quem é maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O {}maior{} valor foi {}.' .format(cores['vermelho'], cores['limpa'], maior))

print('-=-' *20)