matriz=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        matriz[i][j]=int(input('Digite o elemento:  [' + str(i) + ']['+ str(j) +']: '))
print('\n')
v=int(input('Digite um número para multiplicar os elementos da diagonal principal: '))
for i in range(3):
    for j in range(3):
        if i==j:
            matriz[i][j]=v*matriz[i][j]
print(matriz)        

