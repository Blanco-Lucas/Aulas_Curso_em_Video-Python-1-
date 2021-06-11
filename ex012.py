# Aplicador de descontos, 5% para tal produto a seu valor inteiro
n1 = float(input('Diga me o valor inteiro: '))
por = 1 / (n1 / 5)
valor = n1 - por
print(f'Produto com 5% aplicado, com sucesso\n Valor:R${valor:.3}!\n\n *desconto de{por:}*')
