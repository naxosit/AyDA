#N es el tamaño de la matriz N*N
N = 9

# funcion de utilidad para imprimiar la matriz
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()

#Verifica si es legal asignar un número dado a una fila y columna específicas

def isSafe(grid, row, col, num):

	# Verifica fila
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Verifica la columna
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Verifica cuadricula 3x3
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

#Encuentra las posiciones vacias y las ordena segun el nro de posibles nros que pueden ser colocados en esas posiciones
def findEmpty(grid):
	empty_positions = []
	for row in range(N):
		for col in range(N):
			if grid[row][col] == 0:
				possible_numbers = [num for num in range(1, N+1) if isSafe(grid, row, col, num)]
				empty_positions.append((row, col, possible_numbers))
	empty_positions.sort(key=lambda x: len(x[2]))
	return empty_positions

#Intenta asignar valores a todas las ubicaciones no asignadas de tal manera que cumpla 
#con los requisitos para la solución de Sudoku (no duplicación en filas, columnas y cajas)
def solveSudokuGreedy(grid):
	empty_positions = findEmpty(grid)
	if not empty_positions:
		return True
	row, col, possible_number = empty_positions[0]
	for num in possible_number:
		if isSafe(grid, row, col, num):
			grid[row][col] = num
			if solveSudokuGreedy(grid):
				return True
			grid[row][col] = 0
	return False


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

if (solveSudokuGreedy(grid)):
	printing(grid)
else:
	print("no solution exists ")

    #https://www.geeksforgeeks.org/sudoku-backtracking-7/
	# Este codigo es contribuido por sudhanshgupta2019a y modificado por nosotros
