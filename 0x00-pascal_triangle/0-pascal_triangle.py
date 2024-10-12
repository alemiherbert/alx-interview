#!/usr/bin/python3

"""
Pascal's triangle implementation in python
"""


def pascal_triangle(n):
    _outer = []
    _memory = {}

    def pascal_spot(row, col):
        idx = (row, col)
        if idx in _memory:
            return _memory[idx]
        if col == 1:
            return 1
        if row == col:
            return 1
        up_left = pascal_spot(row - 1, col - 1)
        up_right = pascal_spot(row - 1, col)
        _memory[idx] = up_left + up_right
        return _memory[idx]

    for i in range(1, n + 1):
        _inner = []
        for j in range(1, i + 1):
            _inner.append(pascal_spot(i, j))
        _outer.append(_inner)
    return _outer
