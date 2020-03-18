import random
import math


def simulate_pi():
    for i in range(3, 7):
        success = 0
        n = 10 ** i
        for j in range(0, n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x ** 2 + y ** 2 <= 1:
                success += 1
        pi = 4 * success / n
        error = abs(pi - math.pi) / math.pi * 100
        print('n = 10 ^', i, 'pi = {0:.6f} error = {1:4f} %'.format(pi, error))


if __name__ == '__main__':
    simulate_pi()
