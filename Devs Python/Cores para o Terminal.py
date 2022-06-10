'''
#melhores STYLE para o terminal: 0, 1, 4 e 7:
#0 = none
#1 = bold
#4 = Underline
#7 = Negative

    text                 background
 
30   -   preto           preto    -     40
31   -   vermelho        vermelho -     41
32   -   verde           verde    -     42
33   -   amarelo         amarelo  -     43   
34   -   azul            azul     -     44
35   -   Magenta         Magenta  -     45
36   -   ciano           ciano    -     46
37   -   cinza           cinza    -     47
97   -   branco          branco   -    107

'''
#EXEMPLOS
'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

'''print('\033[1;31;43mOla Mundo!\033[m')
print('\033[0;33;44mOla Mundo!\033[m')'''

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m' .format(a, b))



