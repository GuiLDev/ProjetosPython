matriz1=[[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        matriz1[i][j]= int(input('Digite o elemento [' +str(i) + ' ]['+ str(j) + ']:'))
        print(matriz1)
        print('\n')
matriz2=[[0, 0], [0, 0]]
for k in range(2):
     for p in range(2):
         matriz2[k][p] = int(input('Digite o elemento [' + str(k) + ' ][' + str(p) + ']: '))
         print(matriz2)
         print('\n')
         C = [[0, 0], [0, 0]]
C[0][0] = matriz1[0][0] + matriz2[0][0]
C[1][0] = matriz1[1][0] + matriz2[1][0]
C[0][1] = matriz1[0][1] + matriz2[0][1]
C[1][1] = matriz1[1][1] + matriz2[1][1]
print('A soma das matrizes é: ', C)
