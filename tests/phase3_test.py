#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 3
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import math
import random
import statistics

# ==================================================
#   Phase 3
def phase3(X, L, C, R, cnt):

    #   2*len because test cases use even and odd numbers for X and not X
    n = 2*len(X)
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
    if len(C) < math.log(n, 2)**4:
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
#   Unittest : Parameter
@pytest.mark.parametrize(('n'), [
    #   Randomized input
    2*random.randint(2**9, 2**15),

    #   Manuel input
    2**10, 2**12, 2**14, 2**16
])
# ==================================================
#   Unittest : Test
def test_p3(n):
    for t in range(3):
        X = [i for i in range(0, n, 2)]
        cnt = [0 for _ in range(n)]
        medt = statistics.median(X)
        # ------------------------------------------------------------
        # Testcase 1 : Det -  max(sumL, sumR) > n/2
        # Unlabanced
        if t == 1:
            L = [[i, i + 1] for i in reversed(range(1, int(n/12) + 1, 2))]
            C = [i for i in range(int(n/12) + 1, int(n/10) + 1, 2)]
            R = [[i, i + 1] for i in range(int(n/10) + 1, n + 1, 2)]

            med, cnt, res, s = phase3(X, L, C, R, cnt)

            assert res == 'DET'
            assert med == medt
            assert abs(s) > n / 2

        # ------------------------------------------------------------
        # Testcase 2 : AKS - |C| < log(n)
        elif t == 2:
            L = [[i, i + 1] for i in reversed(range(1, int(n/2) - 3, 2))]
            C = [i for i in range(int(n/2) - 3, int(n/2) + 3, 2)]
            R = [[i, i + 1] for i in range(int(n/2) + 3, n, 2)]

            med, cnt, res, s = phase3(X, L, C, R, cnt)

            assert res == 'AKS'
            assert med == medt
            assert len(C) < math.log(n, 2)

        # ------------------------------------------------------------
        # Testcase 3 : Rek - Neither
        elif t == 3:
            L = [[i, i + 1] for i in reversed(range(1, int(n/12) + 1, 2))]
            C = [i for i in range(int(n/12) + 1, int(n*11/12) + 1, 2)]
            R = [[i, i + 1] for i in range(int(n*11/12) + 1, n, 2)]

            med, cnt, res, s = phase3(X, L, C, R, cnt)

            assert res == 'EXP'
            assert med == -1
            assert len(C) >= math.log(n, 2)
            assert abs(s) <= n/2

    return

# ==================================================
