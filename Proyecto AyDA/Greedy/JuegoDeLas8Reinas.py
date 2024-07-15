# Link de extracción del código: https://github.com/dev-michael-schmidt/n-queens/blob/master/greedy_local.py

# Código modificado para 8 reinas

import random
import numpy as np

class GreedyLocal:
    """

    """
    def __init__(self):
        """

        """
        self.N = 8  # Cambiamos N a 8 para 8 reinas O(1)
        self.initialize()  # O(N^2) ya que llena el tablero con 0 y coloca reinas aleatoriamente

    def __str__(self):
        s = '' #O(1)

        for r in range(self.N): #O(N)
            row = 'Q' if self.board[r][0] == -1 else '.' #O(1)
            for c in range(1, self.N): #O(N)
                if self.board[r][c] != -1:#O(1)
                    row = '{} {}'.format(row, '.') #O(1)
                else:
                    row = '{} {}'.format(row, 'Q') #O(1)
            s = '{}{}\n'.format(s, row) #O(1)

        s = s[:-1]# O(1)
        return s #O(1) complejidad O(N^2) dos bucles anidados recorre todo el tablero

    def solve(self):
        """

        """
        tries = int(self.N / 2)  # O(1) Aquí toma como atributo las 8 reinas definidas anteriormente
        curr = self.find_lowest() #O(N^2)

        while not self.is_solution(): #O(k) k es el numero de iteraciones necesarias
            self.place_lowest() #O(N)
            self.update() #O(N^3)

            last = curr #O(1)
            curr = self.find_lowest() #O(N^2)

            if curr >= last: #O(1)
                tries -= 1 #O(1)

            if not tries: #O(1)
                self.initialize() #O (N^2)
                tries = int(self.N / 2)  # O(1) Aquí también toma como atributo las 8 reinas definidas anteriormente
                curr = self.find_lowest() #O(N^2)


    def initialize(self):
        """

        """
        self.board = np.array([[0 for _ in range(8)] for _ in range(8)], dtype=np.int8)  # O(N^2)
        self.queens = [] #O(1)
        self.minimums = [] #O(1)

        for r in range(self.N): #O(N)
            c = random.randint(0, self.N - 1) #O(1)
            self.board[r][c] = -1 #O(1) 
            self.queens.append([r, c]) #O(1)

        self.update() #O(N^2)

    def update(self):
        """

        """
        count = 0 #O (1)

        for r in range(self.N): #O(N)
            self.board[self.queens[r][0]][self.queens[r][1]] = 0 #O(1)
            for c in range(self.N): #O(1)
                self.board[r][c] = -1 #O(1)
                for k in range(self.N): #O(N)
                    if k != r:
                        count += self.heuristic([self.queens[k][0], self.queens[k][1]])  # Cambiamos self.queens[k] a [self.queens[k][0], self.queens[k][1]] para O(N)
                                                                                         # pasar las coordenadas de la reina correctamente


                count += self.heuristic([r, c]) #O(N)
                self.board[r][c] = -1 if (self.queens[r][0] == r and self.queens[r][1] == c) else count
                count = 0 #O(N)

    def find_lowest(self):
        """

        """
        min = self.board[0][0] if self.board[0][0] != -1 else self.board[0][1]  #O(1)
        self.minimums = [] #O(1)

        for r in range(self.N):#O(N)
            for c in range(self.N):#O(N)
                if self.board[r][c] < min and self.board[r][c] != -1: #O(1)
                    min = self.board[r][c] #O(1)

        for r in range(self.N): #O(N)
            for c in range(self.N): #O(N)
                if self.board[r][c] == min: #O(1)
                    self.minimums.append([r, c]) #O(1)

        return min #O(1)

    def place_lowest(self):
        """

        """

        move = random.randint(0, len(self.minimums) - 1) #O (1)
        row, col = self.minimums[move][0], self.minimums[move][1] #O(1)

        for c in range(self.N): #O(N)
            if self.board[row][c] == -1: #O(1)
                self.board[row][col] = -1 #O(1)
                self.queens[row][0], self.queens[row][1] = row, col #O(1)

                self.board[row][c] = 0 #O(1)
                break #O(1) bucle.que recorre una fila del tablero 

    def heuristic(self, queen):
        """

        """
        count = 0 #O(1)
        for r, c in zip(range(queen[0]+1, self.N), range(queen[1]+1, self.N)): #O(N)
            if self.board[r][c] == -1: #O(1)
                count += 1 #O(1)

        for r, c in zip(range(queen[0]+1, self.N), range(queen[1]-1, -1, -1)): #O(N)
            if self.board[r][c] == -1: #O (1)
                count += 1 #O(1)

        for r in range(queen[0]+1, self.N): #O(N)
            if self.board[r][queen[1]] == -1: #O(1)
                count += 1 #O(1)

        return count #O(1) tres bucles independientes que recorren diagonales y la columna

    def is_solution(self):
        """

        """
        for i in range(self.N):  #O(N)
            if self.heuristic(self.queens[i]): # O(N)
                return False #O(1)

        return True #O(1)

if __name__ == '__main__':
    gl = GreedyLocal()
    gl.solve()
    print(gl)
