nome = input("Digite um nome: ")
print(*input("confirme seu nome: "), sep="\n")
v = len(nome)+1
for l in range(v):
    print(nome[:l])

