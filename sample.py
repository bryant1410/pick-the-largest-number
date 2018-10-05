#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np


def greater_t(x, t_func):
    return x >= t_func()


def greater_uniform_t(x):
    return greater_t(x, np.random.rand)


def greater_normal_t(x):
    return greater_t(x, np.random.normal)


def greater_cauchy_t(x):
    return greater_t(x, np.random.standard_cauchy)


def predicted(X, Y, greater_func):
    n = X.shape[0]

    c = 0
    for i in range(n):
        if greater_func(X[i]) == (X[i] >= Y[i]):
            c += 1
    return c / n


def main():
    n = 1000000
    print("Number of samples:", n)
    print("Player 1 and 2 use U(0, 1):", predicted(np.random.rand(n), np.random.rand(n), greater_uniform_t))
    print("Player 1 use N(0, 1) and Player 2 use U(0, 1):", predicted(np.random.normal(size=n), np.random.normal(size=n), greater_uniform_t))
    print("Player 1 use U(0, 1) and Player 2 use N(0, 1):", predicted(np.random.rand(n), np.random.rand(n), greater_normal_t))
    print("Player 1 and 2 use N(0, 1):", predicted(np.random.normal(size=n), np.random.normal(size=n), greater_normal_t))
    print("Player 1 use U(100, 200) and Player 2 use N(0, 1):", predicted(np.random.rand(n) * 100 + 100, np.random.rand(n) * 100 + 100, greater_normal_t))
    print("Player 1 use U(100, 200) and Player 2 use C(0, 1):", predicted(np.random.rand(n) * 100 + 100, np.random.rand(n) * 100 + 100, greater_cauchy_t))
    print("Player 1 use U(1, 2) and Player 2 use N(0, 1):", predicted(np.random.rand(n) + 1, np.random.rand(n) + 1, greater_normal_t))
    print("Player 1 use U(1, 2) and Player 2 use C(0, 1):", predicted(np.random.rand(n) + 1, np.random.rand(n) + 1, greater_cauchy_t))


if __name__ == '__main__':
    main()
