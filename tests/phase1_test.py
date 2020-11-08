#!/usr/bin/python3
# ==================================================
"""
File: RMedian - Unittest - Phase 1
Author: Julian Lorenz
"""
# ==================================================
#   Import
import math
import random
import pytest

# ==================================================
#   Phase 1
def phase1(X, k, d):
    #   Initiation
    n = len(X)
    random.shuffle(X)
    S = X[:k]
    XS = X[k:]
    S.sort()

    #   Keeping the list entries below k/2
    if 2*(k*math.log2(n))**0.5 < k/2:
        lst = [2*(k*math.log2(n))**0.5]
        if 3*(k*math.log2(n))**0.5 < k/2:
            lst.append(3*(k*math.log2(n))**0.5)
            while d*lst[len(lst) - 1] < k/2:
                lst.append(d*lst[len(lst) - 1])
        lst.append(k/2)
    else:
        lst = [k/2]

    #   Buckets
    L = [[] for _ in range(len(lst) - 1)]
    R = [[] for _ in range(len(lst) - 1)]
    C = []

    for s in S[math.floor(k / 2 - lst[0]): math.ceil(k / 2 + lst[0])]:
        C.append(s)

    for i in range(1, len(lst)):
        for s in S[math.floor(k / 2 - lst[i]): math.floor(k / 2 - lst[i - 1])]:
            L[i - 1].append(s)
        for s in S[math.ceil(k / 2 + lst[i - 1]): math.ceil(k / 2 + lst[i])]:
            R[i - 1].append(s)

    return S, XS, L, C, R

# ==================================================
#   Unittest : Parameter
@pytest.mark.parametrize(('n'), [
    #   Randomized input
    random.randint(2**9, 2**15),

    #   Manuel input
    2**10, 2**12, 2**14, 2**12 + 1, 2**12 - 1
])
# ==================================================
#   Unittest : Test
def test_p1(n):
    #   Generating Tastcase

    X0 = [i for i in range(n)]
    k0 = int(n ** (2 / 3))
    d0 = int(n ** (1 / 12))
    S0, XS0, L0, C0, R0 = phase1(X0, k0, d0)

    X1 = [i for i in range(n)]
    k1 = int(n / math.log(n, 2)**(1/3))
    d1 = int(math.log(n, 2)**(1/3))
    S1, XS1, L1, C1, R1 = phase1(X1, k1, d1)

    sumL0, sumR0, sumL1, sumR1 = 0, 0, 0, 0

    for l0 in L0:
        sumL0 += len(l0)

    for l1 in L1:
        sumL1 += len(l1)

    for r0 in R0:
        sumR0 += len(r0)

    for r1 in R1:
        sumR1 += len(r1)

    #   Test
    assert sumL0 == sumR0                           # ||L|| = ||R||
    assert sumL1 == sumR1                           # ||L|| = ||R||
    assert len(L0) == len(R0)                       # |L| = |R|
    assert len(L1) == len(R1)                       # |L| = |R|
    assert sumL0 + len(C0) + sumR0 == k0            # |L| + |C| + |R| = k
    assert sumL1 + len(C1) + sumR1 == k1            # |L| + |C| + |R| = k
    return

# ==================================================
