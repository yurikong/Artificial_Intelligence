import numpy as np


def partA():
    print('Part A. The sampling probabilities\n'
          'P(C|-s,r) = <0.878049, 0.121951>\n'
          'P(C|-s,-r) = <0.310345, 0.689655>\n'
          'P(R|c,-s,w) = <1, 0>\n'
          'P(R|-c,-s,w) = <1, 0>\n')


def partB():
    print('Part B. The transition probability matrix\n'
          '\tS1\t\t\tS2\t\t\tS3\t\t\tS4\n'
          'S1\t0.344828\t0.5\t\t\t0.155172\t0\n'
          'S2\t0\t\t\t0.560976\t0\t\t\t0.439024\n'
          'S3\t0.344828\t0\t\t\t0.155172\t0.5\n'
          'S4\t0\t\t\t0.060976\t0\t\t\t0.939024\n')


def partC():
    n = 1000000
    count = 0
    state = np.random.randint(2, size=4).tolist()
    state[1] = 0
    state[3] = 1
    states = [[0, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1], [1, 0, 1, 1]]
    for i in range(0, n):
        if state == states[0]:
            p = [0.344828, 0.5, 0.155172, 0]
        if state == states[1]:
            p = [0, 0.560976, 0, 0.439024]
        if state == states[2]:
            p = [0.344828, 0, 0.155172, 0.5]
        if state == states[3]:
            p = [0, 0.060976, 0, 0.939024]
        index = np.random.choice(a=range(4), size=1, p=p)[0]
        if index == 0:
            state = states[0]
        if index == 1:
            state = states[1]
        if index == 2:
            state = states[2]
        if index == 3:
            state = states[3]
        if state[0] == 1 and state[1] == 0 and state[3] == 1:
            count += 1
    p = count / n
    print('Part C. The probability for the query\n'
          'P(C|-s,w) = <{0:6f}, {1:6f}>'.format(p, 1-p))


if __name__ == '__main__':
    partA()
    partB()
    partC()