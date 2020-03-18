from board import Board
import numpy as np


class Genetic:

    def __init__(self, n):
        self.n_queen = n
        self.n = 4                      # n genes in pool
        self.goal = n * (n - 1) // 2    # max number of non-attacking queens
        self.steps = 0
        self.boards = []        # board states
        self.encoded = []       # encoded board states
        self.fitness = []
        for i in range(self.n):
            brd = Board(self.n_queen)
            brd.set_queens()
            brd.fitness()
            self.boards.append(brd)
            self.fitness.append(brd.fit)
        self.initial_boards = np.copy(self.boards).tolist()

    def assess(self):
        if self.goal in self.fitness:  # success
            return self.fitness.index(self.goal)  # return index of successful board
        if len(set(self.boards)) == 1:
            return -1  # error
        return -2  # not done

    def encode(self):       # encode board state
        encoded = []
        for brd in self.boards:
            code = ''
            for i in range(self.n_queen):
                for j in range(self.n_queen):
                    if brd.map[i][j] == 1:
                        code += str(j + 1)
            encoded.append(code)
        self.encoded = np.copy(encoded).tolist()

    def selection(self):        # select from pool with chance
        chance = []
        num = sum(self.fitness)
        for fit in self.fitness:
            chance.append(fit / num)
        self.encoded = np.random.choice(self.encoded, self.n, True, p=chance).tolist()

    def crossover(self):        # cross-over by pairs
        pos = self.n_queen // 2
        ind = self.n // 2
        encoded = np.copy(self.encoded).tolist()
        for i in range(0, ind, 2):
            code_a = encoded[i]
            code_b = encoded[i + 1]
            self.encoded[i] = code_a[:pos] + code_b[pos:]
            self.encoded[i + 1] = code_b[:pos] + code_a[pos:]
        pos = self.n_queen - pos
        for i in range(ind, self.n, 2):
            code_a = encoded[i]
            code_b = encoded[i + 1]
            self.encoded[i] = code_a[:pos] + code_b[pos:]
            self.encoded[i + 1] = code_b[:pos] + code_a[pos:]

    def mutation(self):     # mutate randomly
        encoded = np.copy(self.encoded).tolist()
        for i in range(self.n):
            mutate = np.random.randint(0, 2)
            if mutate == 1:
                pos = np.random.randint(0, self.n_queen)
                m_char = str(np.random.randint(1, self.n_queen + 1))
                code = encoded[i]
                self.encoded[i] = code[:pos] + m_char + code[pos + 1:]
        self.steps += 1

    def decode(self):       # convert the encoded board state into board
        boards = []
        fitness = []
        n = self.n_queen
        for code in self.encoded:
            brd = Board(n)
            for i in range(n):
                j = int(code[i]) - 1
                brd.map[i][j] = 1
            brd.fitness()
            fitness.append(brd.fit)
            boards.append(brd)
        self.boards = np.copy(boards).tolist()
        self.fitness = np.copy(fitness).tolist()

    def show(self):     # print board info
        print('encoded:\t', self.encoded)
        print('fitness:\t', self.fitness)
        print('steps:', self.steps)
        print()

    def grab(self, index):      # format to expected output
        ibrd = self.initial_boards[index]
        brd = self.boards[index]
        map = brd.map
        res = ''
        for i in range(self.n_queen):
            res += '\n'
            for j in range(self.n_queen):
                if map[i][j] == 0:
                    res += '- '
                else:
                    res += str(map[i][j]) + ' '
        print('Initial board:')
        ibrd.show()
        print('\nFinal board:')
        print(res[1:])
        print('Fitness:', brd.fit)
        print('Steps:', self.steps)


if __name__ == '__main__':
    n = 5
    genetic = Genetic(n)
    flag = genetic.assess()
    while flag < 0:
        if flag == -1:
            print('All boards are identical. Exiting...')
            break
        genetic.encode()
        genetic.selection()
        genetic.crossover()
        genetic.mutation()
        genetic.decode()
        flag = genetic.assess()
    genetic.grab(flag)
