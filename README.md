# RMedian-Algorithm

![GitHub status](https://img.shields.io/badge/status-release-success) ![GitHub top language](https://img.shields.io/github/languages/top/jfklorenz/python-RMedian) ![Travis](https://travis-ci.org/jfklorenz/RMedian-Algorithm.svg?branch=master) ![GitHub](https://img.shields.io/github/license/jfklorenz/python-RMedian)

A **Python** implementation of the **RMedian algorithm**.

The algorithm is presented in the paper **Fragile Complexity of Comparison-Based Algorithms** by Prof. Dr. Ulrich Meyer and others in 2019, which can can be found on [arXiv.org](https://arxiv.org/abs/1901.02857 "arXiv.org").

It introduces the algorithm *RMedian* and also the concept of *fragile complexity*, i.e. the amount of times an element has been compared during the process of the algorithm.

The package was published on **PyPI** and tested on **Travis CI**.

---

Folder | Content
--- | ---
data | all experimental data as *.csv* files
docs | scientific paper presenting the algorithm (old & new version)  |  
jupyter | *Jupyter Notebook* validation and test files
poster | design for a poster explaining the algorithm  |  
src | *Python* source code
tests | *PyTest* test files

---

## Algorithm


---

## Complexity
1. *Runtime:* RMedian requires linear work w(n) = O(n).
2. Let k(n) = n_ε for 0 < ε ≤ 1/2. Then RMedian requires E(f_min(n)) = O(ε−1loglog(n)) comparisons for the minimum and E(f_rem(n)) = O(n_ε) for the remaining elements.
3. Let k(n) = logn/loglogn. Then RMedian requires E(f_min(n)) = O(log(n)/loglog(n)) comparisons for the minimum and E(f_rem(n)) = O(log(n)/loglog(n)) for the remaining elements.
