# Ler duas notas e calcular a média
math, lp =float(input('Nota de matemática: ')), float(input('Nota de Português: '))
nota = (math + lp)/2
print(nota)
if nota >= 6:
    print('passou')
else:
    print('Não passou')


