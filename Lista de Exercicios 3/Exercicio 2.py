vetor = []
mult = 1
soma = 0

for x in range(5):
    vetor.append(int(input('Insira os numeros: ')))

for v in vetor:
    soma += v
    mult *= v

print('A soma dos números é: ', soma)
print('A multiplicação dos números é: ', mult)
print(vetor)

