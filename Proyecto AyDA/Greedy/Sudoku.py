import psutil
import os
import time

#N es el tamaño de la matriz N*N
N = 9

# funcion de utilidad para imprimiar la matriz
def printing(arr):
	for i in range(N): # O(N)
		for j in range(N): # O(N)
			print(arr[i][j], end = " ") # O(1)
		print() # O(1)

#Verifica si es legal asignar un número dado a una fila y columna específicas

def isSafe(grid, row, col, num):

	# Verifica fila
	for x in range(9): # O(N)
		if grid[row][x] == num: # O(1)
			return False # O(1)

	# Verifica la columna
	for x in range(9): # O(N)
		if grid[x][col] == num: # O(1)
			return False # O(1)
 
	# Verifica cuadricula 3x3
	startRow = row - row % 3 # O(1)
	startCol = col - col % 3 # O(1)
	for i in range(3): # O(1)
		for j in range(3): # O(1)
			if grid[i + startRow][j + startCol] == num: # O(1)
				return False # O(1)
	return True # O(1)

#Encuentra las posiciones vacias y las ordena segun el nro de posibles nros que pueden ser colocados en esas posiciones
def findEmpty(grid):  # O(1)
	empty_positions = []  # O(N)
	for row in range(N):  # O(N)
		for col in range(N): # O(N)
			if grid[row][col] == 0:  # O(1)
				possible_numbers = [num for num in range(1, N+1) if isSafe(grid, row, col, num)] # O(N^2)
				empty_positions.append((row, col, possible_numbers)) # O(1)
	empty_positions.sort(key=lambda x: len(x[2])) # O(N^2 log N^2)
	return empty_positions # O(1)

#Intenta asignar valores a todas las ubicaciones no asignadas de tal manera que cumpla 
#con los requisitos para la solución de Sudoku (no duplicación en filas, columnas y cajas)
def solveSudokuGreedy(grid):
    empty_positions = findEmpty(grid)  # O(N^3)
    if not empty_positions:  # O(1)
        return True  # O(1)
    row, col, possible_number = empty_positions[0]  # O(1)
    for num in possible_number:  # O(N)
        if isSafe(grid, row, col, num):  # O(N)
            grid[row][col] = num  # O(1)
            if solveSudokuGreedy(grid):  # O(N^5)
                return True  # O(1)
            grid[row][col] = 0  # O(1)
    return False  # O(1)


# Driver Code

# 0 significa celdas no asignadas
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


if (solveSudokuGreedy(grid)):
	printing(grid)
else:
	print("no solution exists ")

end_time = time.time()
end_memory = process.memory_info().rss

print(f"Memory used: {end_memory - start_memory} bytes")
print(f"Execution time: {end_time - start_time} seconds")


	#COMPLEJIDAD ALGORITMICA O(N^5)
	
    #https://www.geeksforgeeks.org/sudoku-backtracking-7/
	# Este codigo es contribuido por sudhanshgupta2019a y modificado por nosotros
