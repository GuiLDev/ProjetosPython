print('=' * 50)

larg = float(input('Largura da parede: '))
Alt = float(input('Altura da parede: '))
área = larg * Alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².'.format(larg, Alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta' .format(tinta))

print('=' * 50)

