from board import Board

def h(map):
    queens = []

    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 1:
                queens.append((i, j))

    pairs = set()
    for idx in range(len(queens)):
        for idx2 in range(idx, len(queens)):
            pairs.add((idx, idx2))

    nonattacking_pairs = 0
    for pair in pairs:
        if not conflict(queens[pair[0]], queens[pair[1]]):
            #print("queen1 = " + str(queens[pair[0]]) + "  queen2 = " + str(queens[pair[1]]))
            nonattacking_pairs += 1

    return nonattacking_pairs

def conflict(queen1, queen2):
    horizontal = queen1[1] == queen2[1]
    vertical = queen1[0] == queen2[0]
    diagonal = abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])
    return horizontal or vertical or diagonal

