#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np

n = 1000000
X = np.random.rand(n)
Y = np.random.rand(n)
T = np.random.rand(n)

win = np.average((X >= Y) & (X >= T) | (X < Y) & (X < T))

print(win)

