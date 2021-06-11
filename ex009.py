# ler um número e dizer sua tabuada
n1 = int(input('Digite seu termo: '))
tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10 = n1 * 1, n1 * 2, n1 * 3, n1 * 4, n1 * 5, n1 * 6, n1 * 7, n1 * 8,\
                                                    n1 * 9, n1 * 10
print(f'Tabuada do {n1}!\n{n1} x 1 = {tb1}\n{n1} x 2 = {tb2}\n{n1} x 3 = {tb3}\n{n1} x 4 = {tb4} ', end='')
print(f'\n{n1} x 5 = {tb5}\n{n1} x 6 = {tb6}\n{n1} x 7 = {tb7}\n{n1} x 8 = {tb8}\n{n1} x 9 = {tb9}', end='')
print(f'\n{n1} x 10 = {tb10}')
