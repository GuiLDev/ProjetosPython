pVetor = [] 
sVetor = []
tVetor = []

for p in range(10):
    pVetor.append(input("Digite o elemento da " + str(p + 1) + "ª posição do primeiro vetor: "))
print('-__-'*32)
for k in range(10):
    sVetor.append(input("Digite o elemento da " + str(k + 1) + "ª posição do segundo vetor: "))
print('-__-'*32)
for l in range(10):
    tVetor.append(pVetor[l])
    tVetor.append(sVetor[l])
print('-__-'*32)
print(tVetor)