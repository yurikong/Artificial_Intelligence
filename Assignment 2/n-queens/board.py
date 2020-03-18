import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = n * (n-1) / 2

    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    m = i + 1
                    n = j
                    while m < self.n_queen:
                        if self.map[m][n] == 1:
                            self.fit -= 1
                        m += 1

                    m = i + 1
                    n = j + 1
                    while m < self.n_queen and n < self.n_queen:
                        if self.map[m][n] == 1:
                            self.fit -= 1
                        m += 1
                        n += 1

                    m = i + 1
                    n = j - 1
                    while m < self.n_queen and n >= 0:
                        if self.map[m][n] == 1:
                            self.fit -= 1
                        m += 1
                        n -= 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit)


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.fitness()
    test.show()
