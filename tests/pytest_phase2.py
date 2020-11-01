#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 1 & 2
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import random
import math

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
#   Phase 2
def phase2(S, XS, L, C, R, cnt):

    mark = [False for _ in range(len(XS) + len(S))]
    b = len(L)

    random.shuffle(XS)
    for x_i in XS:
        med = 0
        for j in reversed(range(0, b - 1)):

            current = 2 ** 50
            random.shuffle(L[j])
            for l in L[j]:
                if cnt[l] < current:
                    x_A = l

            if mark[x_A] == True:
                c = 1

            else:
                c = 2

            cnt[x_i] += 1
            cnt[x_A] += 1

            if x_i < x_A:
                if j + c < b:
                    mark[x_i] = True
                    L[j + c].append(x_i)
                    med = -1
                else:
                    med = -2
                break

            current2 = 2 ** 50
            random.shuffle(R[j])
            for r in R[j]:
                if cnt[r] < current2:
                    x_B = r

            if mark[x_B] == True:
                c = 1
            else:
                c = 2

            cnt[x_i] += 1
            cnt[x_B] += 1

            if x_i > x_B:
                if j + c < b:
                    mark[x_i] = True
                    R[j + c].append(x_i)
                    med = 1
                else:
                    med = 2
                break
        if med == 0:
            C.append(x_i)
        elif med == -2:
            L[len(L) - 1].append(x_i)
        elif med == 2:
            R[len(R) - 1].append(x_i)
    return S, XS, L, C, R, cnt

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
    cnt0 = [0 for _ in range(n)]
    k0 = int(n ** (2 / 3))
    d0 = int(n ** (1 / 12))
    S0, XS0, L0, C0, R0, = phase1(X0, k0, d0)
    S0, XS0, L0, C0, R0, cnt0 = phase2(S0, XS0, L0, C0, R0, cnt0)

    X1 = [i for i in range(n)]
    cnt1 = [0 for _ in range(n)]
    k1 = int(n / math.log(n, 2)**(1/3))
    d1 = int(math.log(n, 2)**(1/3))
    S1, XS1, L1, C1, R1 = phase1(X1, k1, d1)
    S1, XS1, L1, C1, R1, cnt1 = phase2(S1, XS1, L1, C1, R1, cnt1)

    if n % 2 == 0:
        assert int((n / 2) + 1) in C0
        assert int((n / 2) + 1) in C1
        assert cnt0[int((n / 2) + 1)] <= len(L0) + len(R0)
        assert cnt1[int((n / 2) + 1)] <= len(L1) + len(R1)
    elif n % 2 == 1:
        assert int(n / 2) in C0
        assert int(n / 2) in C1
        assert cnt0[int(n / 2)] <= len(L0) + len(R0)
        assert cnt1[int(n / 2)] <= len(L1) + len(R1)

    #   Test
    return

# ==================================================
