n1, n2 = int(input('Primeiro valor: ')), int(input('Segundo valor: '))
a, s, d, di, m, p, r = n1 + n2, n1 - n2, n1 / n2, n1 // n2, n1 * n2, n1 ** n2, n1**(1/n2)
print(f'Soma: {a}\nSubitração: {s}\nDivisão: {d:.3}\nMultiplicação: {m}\nDivisão exata: {di}\nPotência: {p}', end='')
print(f'\nRaiz ao {n2} é: {r:.5} :)')
