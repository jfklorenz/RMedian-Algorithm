#!/usr/bin/python3
# ==================================================
"""
File: RMedian - Phase 2
Author: Julian Lorenz
"""
# ==================================================
#   Import
import random

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
