def is_valid(board, row, col, num):
    for x in range(9):  # 1 OE (inicialización del bucle) + 9 OE (iteraciones del bucle)
        if board[row][x] == num:  # 1 OE (acceso a la matriz) + 1 OE (comparación) * 9 = 18 OE
            return False  # 1 OE (retorno)
        if board[x][col] == num:  # 1 OE (acceso a la matriz) + 1 OE (comparación) * 9 = 18 OE
            return False  # 1 OE (retorno)
        if board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:  # 5 OE (cálculos y acceso a la matriz) + 1 OE (comparación) * 9 = 54 OE
            return False  # 1 OE (retorno)
    return True  # 1 OE (retorno)

def branch_and_bound(board):
    empty_cell = find_empty(board)  # 1 OE (llamada a la función)
    if not empty_cell:  # 1 OE (comparación)
        return True  # 1 OE (retorno)

    row, col = empty_cell  # 1 OE (asignación)
    for num in range(1, 10):  # 1 OE (inicialización del bucle) + 9 OE (iteraciones del bucle)
        if is_valid(board, row, col, num):  # 1 OE (llamada a la función) * 9 = 9 OE
            board[row][col] = num  # 1 OE (acceso a la matriz) + 1 OE (asignación) * 9 = 18 OE

            if branch_and_bound(board):  # 1 OE (llamada a la función) * 9 = 9 OE
                return True  # 1 OE (retorno)

            board[row][col] = 0  # 1 OE (acceso a la matriz) + 1 OE (asignación) * 9 = 18 OE

    return False  # 1 OE (retorno)

def find_empty(board):
    for i in range(9):  # 1 OE (inicialización del bucle) + 9 OE (iteraciones del bucle)
        for j in range(9):  # 1 OE (inicialización del bucle) + 9 OE (iteraciones del bucle) * 9 = 90 OE
            if board[i][j] == 0:  # 1 OE (acceso a la matriz) + 1 OE (comparación) * 81 = 162 OE
                return (i, j)  # 1 OE (retorno)
    return None  # 1 OE (retorno)

def print_board(board):
    for row in board:  # 1 OE (inicialización del bucle) + 9 OE (iteraciones del bucle)
        print(" ".join(str(num) for num in row))  # 1 OE (llamada a la función) * 9 = 9 OE

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if branch_and_bound(board):  # 1 OE (llamada a la función)
    print("Sudoku solved successfully:")  # 1 OE (llamada a la función print)
    print_board(board)  # 1 OE (llamada a la función)
else:
    print("No solution exists for the given Sudoku.")  # 1 OE (llamada a la función print)
