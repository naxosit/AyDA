# Programa de backtracking en Python para resolver el problema de Sudoku

# Función de utilidad para imprimir el tablero
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

# Función para encontrar una celda no asignada en el tablero
# Busca en el tablero para encontrar una celda no asignada.
# Si encuentra una, las variables de referencia row y col se establecen
# en la ubicación no asignada, y se devuelve True. Si no quedan entradas
# no asignadas, se devuelve False.
# 'l' es una lista que se pasa desde la función solve_sudoku
# para llevar un registro de la fila y la columna.
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

# Devuelve un booleano que indica si alguna entrada asignada
# en la fila especificada coincide con el número dado.
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False

# Devuelve un booleano que indica si alguna entrada asignada
# en la columna especificada coincide con el número dado.
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False

# Devuelve un booleano que indica si alguna entrada asignada
# dentro del cuadro 3x3 especificado coincide con el número dado.
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False

# Comprueba si será legal asignar num a la fila y columna dadas.
# Devuelve un booleano que indica si será legal asignar
# num a la ubicación de fila y columna dadas.
def check_location_is_safe(arr, row, col, num):
    # Comprueba si 'num' no está ya colocado en la fila actual,
    # columna actual y cuadro 3x3 actual
    return (not used_in_row(arr, row, num) and
            not used_in_col(arr, col, num) and
            not used_in_box(arr, row - row % 3, col - col % 3, num))

# Toma un tablero parcialmente completado y
# trata de asignar valores a todas las ubicaciones no asignadas
# de tal manera que se cumplan los requisitos
# para la solución de Sudoku (no duplicación
# en filas, columnas y cuadros).
def solve_sudoku(arr):
    # 'l' es una lista que mantiene el
    # registro de la fila y columna en la
    # función find_empty_location
    l = [0, 0]
    
    # Si no hay ubicación no asignada, hemos terminado
    if not find_empty_location(arr, l):
        return True
    
    # Asignando valores de lista a fila y columna
    # que obtuvimos de la función anterior
    row = l[0]
    col = l[1]
    
    # Considera dígitos del 1 al 9
    for num in range(1, 10):
        # Si parece prometedor
        if check_location_is_safe(arr, row, col, num):
            # Hace una asignación tentativa
            arr[row][col] = num

            # Devuelve True si tiene éxito
            if solve_sudoku(arr):
                return True

            # En caso de fallo, deshace la asignación e intenta de nuevo
            arr[row][col] = 0
    
    # Esto dispara el backtracking
    return False

# Función principal para probar las funciones anteriores
if __name__ == "__main__":
    # Creando un array 2D para el tablero
    grid = [[0 for x in range(9)] for y in range(9)]
    
    # Asignando valores al tablero
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    # Si tiene éxito, imprime el tablero
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")

    #https://www.geeksforgeeks.org/sudoku-backtracking-7/
	# Este codigo es contribuido por sudhanshgupta2019a y modificado por nosotros