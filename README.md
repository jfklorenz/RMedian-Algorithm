# RMedian-Algorithm

![GitHub status](https://img.shields.io/badge/status-release-success) ![GitHub top language](https://img.shields.io/github/languages/top/jfklorenz/python-RMedian) ![Travis](https://travis-ci.org/jfklorenz/RMedian-Algorithm.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/RMedian-Algorithm.svg)](https://badge.fury.io/py/RMedian-Algorithm) ![Liscence](https://img.shields.io/github/license/jfklorenz/RMedian-Algorithm)

A **Python** implementation of the **RMedian algorithm**.

The algorithm is presented in the paper **Fragile Complexity of Comparison-Based Algorithms** by Prof. Dr. Ulrich Meyer and others in 2019, which can can be found on [arXiv.org](https://arxiv.org/abs/1901.02857 "arXiv.org").

It introduces the algorithm *RMedian* and also the concept of *fragile complexity*, i.e. the amount of times an element has been compared during the process of the algorithm.

RMedian is a randomized recursive algorithm that finds the median element of a given total orderer set of elements. The algorithm has a tuning parameter k(n) controlling the trade-pff between the expected fragile complexity f_med(n) of the median element and the maximum expected fragile complexity f_rem(n) of the remaining non-median elements; if n is clear from the context, we use k instead of k(n).

The included paper provides further details regarding the work and fragile complexity of various inputs.

Folder | Content
--- | ---
data | all experimental data as *.csv* files
docs | scientific paper presenting the algorithm (old & new version)
jupyter | *Jupyter Notebook* validation and test files
poster | design for a poster explaining the algorithm
src | *Python* source code
tests | *PyTest* test files

The package was published on **PyPI** and tested on **Travis CI**.
