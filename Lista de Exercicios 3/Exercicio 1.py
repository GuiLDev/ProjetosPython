mediasAlunos = []
alunosAcimaDaMedia = 0

for aluno in range(3):
	somaDasNotas = 0
	
	print(aluno+1, 'º aluno')
	for nota in range(4):
		somaDasNotas += float(input("Digite a nota do aluno: "))
	
	mediasAlunos.append(somaDasNotas/4)
	
	if mediasAlunos[aluno] >= 7:
		alunosAcimaDaMedia += 1

print('O número de alunos acima da média é de: ', alunosAcimaDaMedia)

