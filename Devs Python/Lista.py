print('-=-' * 30)

num_alunos = 3
nomes = []
notas = []
media = 0

for i in range(num_alunos):
    nomes.append(str(input("Informe o nome do aluno: ")))
    notas.append(float(input("Informe a nota de " + nomes[i] + ': ')))
    print('~' * 35)
    media = media + notas[i]
media = media / num_alunos
print("A media da turma é {:.2f}" .format(media))

for i in range(num_alunos):
    if notas[i] > media:
        print("Parabens!", nomes[i])
    else:
        print("Está de recuperação " + nomes[i] + '!')
        
print('-=-' * 30)
