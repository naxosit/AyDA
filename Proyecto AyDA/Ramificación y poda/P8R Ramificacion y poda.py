""" Programa en Python3 para resolver el Problema de las 8 Reinas usando Ramificación y Poda """
# Código extraído de https://www.geeksforgeeks.org/n-queen-problem-using-branch-and-bound/

N = 8    # Define el tamaño del tablero (8x8)

# La funcion "printSolution" --> Imprime la solución del tablero.
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end = " ") 
        print() 

# La funcion "isSafe" --> Verifica si es seguro colocar una reina en una posición (row, col).     -> Utiliza tres estructuras auxiliares:
def isSafe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):   #slashCode y backslashCode :Identifican las diagonales.
    if (slashCodeLookup[slashCode[row][col]] or                                                    #rowLookup: Indica si una fila ya está ocupada.
        backslashCodeLookup[backslashCode[row][col]] or                                            #slashCodeLookup y backslashCodeLookup: Indican si una diagonal ya está ocupada.
        rowLookup[row]): 
        return False
    return True

# La funcion "solveNQueensUtil"  --> Función recursiva principal que implementa la lógica de ramificación y poda.

def solveNQueensUtil(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup): 
                        
    """ Caso base: Si todas las reinas están colocadas  --> se encontro una solucion completa"""
    if(col >= N): 
        return True               
    
    #intento de colocar las reinas en las filas i de la columna actual                                     
    for i in range(N):  

        # Verifica si es seguro colocar una reina en board[i][col]
        if(isSafe(i, col, slashCode, backslashCode, 
                rowLookup, slashCodeLookup, 
                backslashCodeLookup)): 
                    
            """ Si es seguro --> Actualizacion del tablero: Coloca esta reina en board[i][col] """
            board[i][col] = 1
            #Actualización de Estructuras Auxiliares  
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True
            
            """ Recursivamente intenta colocar el resto de las reinas """
            if(solveNQueensUtil(board, col + 1, 
                                slashCode, backslashCode, 
                                rowLookup, slashCodeLookup, 
                                backslashCodeLookup)): 
                #Devuelve True si se logro encontrar una solucion completa
                return True
            
            """ Si colocar la reina en board[i][col]  no conduce a una solución, entonces retrocede """
            
            """ Elimina la reina de board[i][col] """
            board[i][col] = 0
            rowLookup[i] = False
            #Actualización de Estructuras Auxiliares  
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False
            
    """ Si no se puede colocar la reina en ninguna fila en  esta columna col, entonces devuelve False """
    return False

#La funcion "solveNQueens"  -> Inicializa las estructuras de datos  necesarias para el tablero y las diagonales..
#--> Con el fin permitir visualizar y manipular la disposición de las reinas en el tablero, Facilitar la comprobación rápida de las diagonales y verificar rápidamente si una posición es segura
def solveNQueens(): 

    board = [[0 for i in range(N)] for j in range(N)]                     # matriz N x N inicializada con ceros, donde se colocarán las reinas.
    slashCode = [[0 for i in range(N)]  for j in range(N)]                # matrices N x N utilizadas para identificar las diagonales 
    backslashCode = [[0 for i in range(N)] for j in range(N)]             # principales y secundarias respectivamente.
    rowLookup = [False] * N                                               # array de tamaño N que indica si una fila está ocupada.
    x = 2 * N - 1
    slashCodeLookup = [False] * x                                         # arrays de tamaño 2*N-1 que indican si una diagonal 
    backslashCodeLookup = [False] * x                                     # principal o secundaria está ocupada.
    
    # Inicializar matrices auxiliares 
    for rr in range(N): 
        for cc in range(N): 
            slashCode[rr][cc] = rr + cc 
            backslashCode[rr][cc] = rr - cc + 7

   # LLamada recursiva 
    if(solveNQueensUtil(board, 0, slashCode, backslashCode, 
                        rowLookup, slashCodeLookup,                      # son los parámetros iniciales, empezando por la columna 0.
                        backslashCodeLookup) == False):         
        print("La solución no existe")                                   #Si solveNQueensUtil retorna False
        return False
        
    # Solución encontrada 
    printSolution(board) 
    return True

# Código del controlador 
solveNQueens() 


#calculo de complejidad temporal T(n)

# T(n) = O(N!) --> donde N es el número de filas y columnas en el tablero cuadrado
"""Esto se debe a que, para cada columna, el algoritmo intenta colocar una reina en cada fila y 
luego intenta de manera recursiva colocar las reinas en las columnas restantes. La cantidad de
 combinaciones posibles de ubicaciones de reinas en el tablero es N!, ya que solo puede haber 
 una reina en cada fila y en cada columna."""