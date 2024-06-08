# Este programa es una traducción de la solución de Nilaus Wirth's en el
# lenguaje de programación de Python, pero no tiene el índice aritmético
# encontrado en el original y en su lugar utiliza listas para mantener el
# código del programa lo más simple posible. 

def Reinas(n: int, i: int, a: list, b: list, c: list):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from Reinas(n, i + 1, a + [j], b + [i + j], c + [i - j])
            else:
                yield a

for solucion in Reinas(8, 0, [], [], []):
    print(solucion)


# Código extraído de https://en.wikipedia.org/wiki/Eight_queens_puzzle#Sample_program
# Otro link de interés: https://stackoverflow.com/questions/75999918/implementing-a-python-algorithm-for-solving-the-n-queens-problem-efficiently