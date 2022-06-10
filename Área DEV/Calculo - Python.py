#operadores artimeticos: +, -, *, /, **, //, %;

# + = Soma
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Exponencial
# // = Divisão Real
# % = Resto de divisão


#Ordens de precedência:
#1: ()
#2: **
#3: *, /, //, %
#4: +, -
print('=' * 50)

n = int (input ('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do valor é {}.' .format(d))
print('O triplo do valor é {}.' .format(t))
print('A raiz quadrada de {} é {:.0f}!' .format(n, r))

print('=' * 50)






