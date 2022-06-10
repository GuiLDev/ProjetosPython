print('-=-' *20)

num = int(input('Me diga um número qualquer: '))
#o resto da divisão em numeros pares sempre dará 0!
#o resto da divisão em numero impares sempre dará 1! 
res = num % 2
if res == 0:
    print('O número {} é PAR!' .format(num))
else:
    print('O número {} é ÍMPAR!' .format(num))

print('-=-' *20)