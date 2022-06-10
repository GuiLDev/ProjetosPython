km = int(input('Quantos Km foram rodados?: '))
dias = float(input('Quantos dias o carro foi alugado?: '))
r1 = (dias * 60) + (km * 0.15)
print('O valor do aluguel é de R${:.2f}'.format(r1))

