print('-=-' *20)
dist = float (input("Qual é a distancia da sua viagem? "))
print("Você está prestes a começar uma viagem de tantos {}Km." .format(dist))
if dist <= 200:
    preço = dist * 0.50 
else:
    preço = dist * 0.45
print('E o preço da sua passagem será de tantos R${:.2f}' .format(preço))
print('-=-' *20)
