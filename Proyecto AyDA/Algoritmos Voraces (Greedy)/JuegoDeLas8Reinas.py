# Link de extracción del código: https://github.com/dev-michael-schmidt/n-queens/blob/master/greedy_local.py

# Queda modificar la variable 'n' por 8, puesto que este código está hecho para 'n' reinas.

import random
import numpy as np

class GreedyLocal:
    """

    """
    def __init__(self, N):
        """

        """
        self.N = N
        self.initialize()

    def __str__(self):
        s = ''

        for r in range(self.N):
            row = 'Q' if self.board[r][0] == -1 else '.'
            for c in range(1, self.N):
                if self.board[r][c] != -1:
                    row = '{} {}'.format(row, '.')
                else:
                    row = '{} {}'.format(row, 'Q')
            s = '{}{}\n'.format(s, row)

        s = s[:-1]
        return s

    def solve(self):
        """

        """
        tries = int(self.N / 2)
        curr = self.find_lowest()

        while not self.is_solution():
            self.place_lowest()
            self.update()

            last = curr
            curr = self.find_lowest()

            if curr >= last:
                tries -= 1

            if not tries:
                self.initialize()
                tries = int(self.N / 2)
                curr = self.find_lowest()


    def initialize(self):
        """

        """
        self.board = np.array([[0 for _ in range(9)] for _ in range(9)], dtype=np.int8)
        self.queens = []
        self.minimums = []

        for r in range(self.N):
            c = random.randint(0, self.N - 1)
            self.board[r][c] = -1
            self.queens.append([r, c])

        self.update()

    def update(self):
        """

        """
        count = 0

        for r in range(self.N):
            self.board[self.queens[r][0]][self.queens[r][1]] = 0
            for c in range(self.N):
                self.board[r][c] = -1
                for k in range(self.N):
                    if k != r:
                        count += self.heuristic(self.queens[k])

                count += self.heuristic([r, c])
                self.board[r][c] = -1 if (self.queens[r][0] == r and self.queens[r][1] == c) else count
                count = 0

    def find_lowest(self):
        """

        """
        min = self.board[0][0] if self.board[0][0] != -1 else self.board[0][1]
        self.minimums = []

        for r in range(self.N):
            for c in range(self.N):
                if self.board[r][c] < min and self.board[r][c] != -1:
                    min = self.board[r][c]

        for r in range(self.N):
            for c in range(self.N):
                if self.board[r][c] == min:
                    self.minimums.append([r, c])

        return min

    def place_lowest(self):
        """

        """

        move = random.randint(0, len(self.minimums) - 1)
        row, col = self.minimums[move][0], self.minimums[move][1]

        for c in range(self.N):
            if self.board[row][c] == -1:
                self.board[row][col] = -1
                self.queens[row][0], self.queens[row][1] = row, col

                self.board[row][c] = 0
                break

    def heuristic(self, queen):
        """

        """
        count = 0
        for r, c in zip(range(queen[0]+1, self.N), range(queen[1]+1, self.N)):
            if self.board[r][c] == -1:
                count += 1

        for r, c in zip(range(queen[0]+1, self.N), range(queen[1]-1, -1, -1)):
            if self.board[r][c] == -1:
                count += 1

        for r in range(queen[0]+1, self.N):
            if self.board[r][queen[1]] == -1:
                count += 1

        return count

    def is_solution(self):
        """

        """
        for i in range(self.N):
            if self.heuristic(self.queens[i]):
                return False

        return True

if __name__ == '__main__':
    gl = GreedyLocal(8)
    gl.solve()
    print(gl)