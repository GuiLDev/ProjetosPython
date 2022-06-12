mediasAlunos = []
alunosAcimaDaMedia = 0

#Faz uma contagem de valor manual entre 3 alunos

for aluno in range(10):
	somaDasNotas = 0
 
	#Faz uma contagem entre 4 notas para cada aluno 
 
	print(aluno+1, 'º aluno')
	for nota in range(4):
		somaDasNotas += float(input("Digite a nota do aluno: "))
	
 	#Divisão das 4 notas por 4 para obter a média
  
	mediasAlunos.append(somaDasNotas/4)
	
	if mediasAlunos[aluno] >= 7:
		alunosAcimaDaMedia += 1
  
	#O Numero de alunos acima da média
 
print('O número de alunos acima da média é de: ', alunosAcimaDaMedia)

