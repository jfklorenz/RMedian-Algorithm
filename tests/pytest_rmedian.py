#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - PyTest - Full Algorithm
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import math
import random
import statistics

# ==================================================
#   RMedian
def rmedian(X, k, d, cnt = [], rec = 0):

    if cnt == []:
        cnt = [0 for _ in range(len(X))]

    S, XS, L, C, R = phase1(X, k, d)
    S, XS, L, C, R, cnt = phase2(S, XS, L, C, R, cnt)

    return phase3(X, k, d, L, C, R, cnt, rec)

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
def phase3(X, k, d, L, C, R, cnt, rec):

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
            return (X[int(len(X) / 2 - 1)] + X[int(len(X) / 2)]) / 2, cnt, res, rec
        else:
            return X[int(len(X) / 2 - 0.5)], cnt, res, rec

    # AKS
    if len(C) < math.log(n) / math.log(2):
        res = 'AKS'
        C.sort()
        if len(C) % 2 == 0:
            return (C[int(len(C) / 2 - 1)] + C[int(len(C) / 2)]) / 2, cnt, res, rec
        else:
            return C[int(len(C) / 2 - 0.5)], cnt, res, rec

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
    rec += 1
    return rmedian(C, k, d, cnt, rec)

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
def test_algo(n):
    #   Generating Testcase

    X0 = [i for i in range(n)]
    k0 = int(n ** (2 / 3))
    d0 = int(n ** (1 / 12))
    med0, cnt0, res0, rec0 = rmedian(X0, k0, d0)

    X1 = [i for i in range(n)]
    k1 = int(n / math.log(n, 2)**(1/3))
    d1 = int(math.log(n, 2)**(1/3))
    med1, cnt1, res1, rec1 = rmedian(X1, k1, d1)

    medt0 = statistics.median(X0)
    medt1 = statistics.median(X1)

    #   Test
    assert med0 == medt0
    assert med1 == medt1

    return

# ==================================================
