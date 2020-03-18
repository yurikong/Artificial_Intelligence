from board import Board
from heuristic import h
import numpy as np

class Hill_Climb:
    def __init__(self):
        self.no_steps = 0


if __name__ == '__main__':
    brd = Board(5)
    brd.set_queens()
    print("Initial board:")
    print(np.matrix(brd.map))

    target = brd.n_queen * (brd.n_queen - 1) // 2

    queens = []
    map = brd.map
    for i in range(brd.n_queen):
        for j in range(brd.n_queen):
            if map[i][j] == 1:
                queens.append([i, j])
    best = h(brd.map)
    rowIdx = 0 #used at end of loop so we change rows each iteration.
    moveCount = 0
    totalMoves = 0

    while best < target:
        #make a board for each possible position in the current row.
        boards = []
        for boardCount in range(brd.n_queen):
            board = np.copy(brd.map)
            for colIdx in range(brd.n_queen):
                if colIdx is boardCount:
                    board[rowIdx][colIdx] = 1
                else:
                    board[rowIdx][colIdx] = 0
            boards.append(board)

        #evaluate each board for the row.
        for board in boards:
            hvalue = h(board)
            if hvalue > best:
                best = hvalue
                brd.map = board

        #loop through the rows
        moveCount += 1
        totalMoves += 1
        if moveCount >= 15: #random restart
            brd.map = [[0 for j in range(brd.n_queen)] for i in range(brd.n_queen)]
            brd.set_queens()
            moveCount = 0
        rowIdx += 1
        if rowIdx is brd.n_queen:
            rowIdx = 0

    print("final board:")
    print(brd.map)
    print("fitness = ", h(brd.map), " target = ", target, " move count = ", totalMoves)

