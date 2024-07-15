import psutil
import os
import time

# Programa de backtracking en Python para resolver el problema de Sudoku

# Función de utilidad para imprimir el tablero
def print_grid(arr):
    for i in range(9):  # O(N)
        for j in range(9):  # O(N)
            print(arr[i][j], end=" ")  # O(1)
        print()  # O(1)

# Función para encontrar una celda no asignada en el tablero
# Busca en el tablero para encontrar una celda no asignada.
# Si encuentra una, las variables de referencia row y col se establecen
# en la ubicación no asignada, y se devuelve True. Si no quedan entradas
# no asignadas, se devuelve False.
# 'l' es una lista que se pasa desde la función solve_sudoku
# para llevar un registro de la fila y la columna.
def find_empty_location(arr, l):
    for row in range(9):  # O(N)
        for col in range(9):  # O(N)
            if arr[row][col] == 0:  # O(1)
                l[0] = row  # O(1)
                l[1] = col  # O(1)
                return True  # O(1)
    return False  # O(1)

# Devuelve un booleano que indica si alguna entrada asignada
# en la fila especificada coincide con el número dado.
def used_in_row(arr, row, num):
    for i in range(9):  # O(N)
        if arr[row][i] == num:  # O(1)
            return True  # O(1)
    return False  # O(1)

# Devuelve un booleano que indica si alguna entrada asignada
# en la columna especificada coincide con el número dado.
def used_in_col(arr, col, num):
    for i in range(9):  # O(N)
        if arr[i][col] == num:  # O(1)
            return True  # O(1)
    return False  # O(1)

# Devuelve un booleano que indica si alguna entrada asignada
# dentro del cuadro 3x3 especificado coincide con el número dado.
def used_in_box(arr, row, col, num):
    for i in range(3):  # O(1)
        for j in range(3):  # O(1)
            if arr[i + row][j + col] == num:  # O(1)
                return True  # O(1)
    return False  # O(1)

# Comprueba si será legal asignar num a la fila y columna dadas.
# Devuelve un booleano que indica si será legal asignar
# num a la ubicación de fila y columna dadas.
def check_location_is_safe(arr, row, col, num):
    # Comprueba si 'num' no está ya colocado en la fila actual,
    # columna actual y cuadro 3x3 actual
    return (not used_in_row(arr, row, num) and  # O(N)
            not used_in_col(arr, col, num) and  # O(N)
            not used_in_box(arr, row - row % 3, col - col % 3, num))  # O(1)

# Toma un tablero parcialmente completado y
# trata de asignar valores a todas las ubicaciones no asignadas
# de tal manera que se cumplan los requisitos
# para la solución de Sudoku (no duplicación
# en filas, columnas y cuadros).
def solve_sudoku(arr):
    # 'l' es una lista que mantiene el
    # registro de la fila y columna en la
    # función find_empty_location
    l = [0, 0] # O(1)
    
    # Si no hay ubicación no asignada, hemos terminado
    if not find_empty_location(arr, l): # O(N^2)
        return True  # O(1)
    
    # Asignando valores de lista a fila y columna
    # que obtuvimos de la función anterior
    row = l[0]  # O(1)
    col = l[1]  # O(1)
    
    # Considera dígitos del 1 al 9
    for num in range(1, 10):  # O(1)
        # Si parece prometedor
        if check_location_is_safe(arr, row, col, num):  # O(N)
            # Hace una asignación tentativa
            arr[row][col] = num  # O(1) 

            # Devuelve True si tiene éxito
            if solve_sudoku(arr):   # O(9^(N^2))
                return True  # O(1)

            # En caso de fallo, deshace la asignación e intenta de nuevo
            arr[row][col] = 0  # O(1)
    
    # Esto dispara el backtracking
    return False  # O(1)

# Función principal para probar las funciones anteriores
if __name__ == "__main__":
    # Creando un array 2D para el tablero
    grid = [[0 for x in range(9)] for y in range(9)]  # O(N^2)
    
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
    
    process = psutil.Process(os.getpid())  
    start_memory = process.memory_info().rss  
    start_time = time.time()

    # Si tiene éxito, imprime el tablero
    if solve_sudoku(grid): # O(9^(N^2))
        print_grid(grid)  #O(N^2)
    else:
        print("No solution exists") 

    end_memory = process.memory_info().rss  
    end_time = time.time()  
    
    print(f"Memory used: {end_memory - start_memory} bytes")  
    print(f"Execution time: {end_time - start_time} seconds")  

    #COMPLEJIDAD ALGORITMICA # O(9^(N^2))  n=9
                            #O(9^81)

    #https://www.geeksforgeeks.org/sudoku-backtracking-7/
	# Este codigo es contribuido por sudhanshgupta2019a y modificado por nosotros