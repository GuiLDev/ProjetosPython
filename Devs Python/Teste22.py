nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiuscula é {}.' .format(nome.upper()))
print('Seu nome em minuscula é {}.' .format(nome.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
print(separa)





