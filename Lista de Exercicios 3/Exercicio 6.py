txt1 = str(input('Digite uma frase: ')).strip()
txt2 = str(input('Digite outra frase: ')).strip()

print("O texto 1 tem {} letras." .format(len(txt1)))
print("O texto 2 tem {} letras." .format(len(txt2)))

if len(txt1) != len(txt2):
    print("As duas frases são de tamanhos diferentes.")
else:
    print("As duas frases são de tamanhos iguais.")
if txt1 != txt2:
    print("As duas strings possuem conteúdos difentes.")
else:
    print("As duas frases são do mesmo conteúdo.")