# Interpretar altura e largura, calcular área e diz qual o valor para a pintura desta área. tinta 1L m²
a, l, p = int(input('Diga-me, altura: ')), int(input('Diga-me, largura: ')), print('*Em metros*')
multiplicação = a * l
print(f'Área de {multiplicação}m².')
valor = multiplicação // 1/2
print(f'São necessarias {valor} litros de tinta')
