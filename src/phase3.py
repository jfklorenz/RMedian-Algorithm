#!/usr/bin/python3
# ==================================================
"""
File: RMedian - Phase 3
Author: Julian Lorenz
"""
# ==================================================
#   Import
import math
import random

# ==================================================
def phase3(X, L, C, R, cnt):

    n = len(X)
    sumL, sumR = 0, 0
    for l in L:
        sumL += len(l)
    for r in R:
        sumR += len(r)

    s = sumL - sumR

    #   Det Median
    if max(sumL, sumR) > n / 2:
        res = 'DET'
        if len(X) % 2 == 0:
            return (X[int(len(X) / 2 - 1)] + X[int(len(X) / 2)]) / 2, cnt, res, s
        else:
            return X[int(len(X) / 2 - 0.5)], cnt, res, s

    # AKS
    if len(C) < math.log(n) / math.log(2):
        res = 'AKS'
        C.sort()
        if len(C) % 2 == 0:
            return (C[int(len(C) / 2 - 1)] + C[int(len(C) / 2)]) / 2, cnt, res, s
        else:
            return C[int(len(C) / 2 - 0.5)], cnt, res, s

    #   Expand
    if s < 0:
        rs = []
        for r in R:
            rs += r
        random.shuffle(rs)
        for i in range(-s):
            C.append(rs[i])
            for r in R:
                if rs[i] in r:
                    r.remove(rs[i])
    else:
        ls = []
        for l in L:
            ls += l
        random.shuffle(ls)
        for i in range(s):
            C.append(ls[i])
            for l in L:
                if ls[i] in l:
                    l.remove(ls[i])

    res = 'EXP'

    return -1, cnt, res, s

# ==================================================
