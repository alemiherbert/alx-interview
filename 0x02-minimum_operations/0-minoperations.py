#!/usr/bin/python3

"""
Minimum operations
"""

def minOperations(n: int) -> int:
    """
    Calculate the number of steps required to get n H characters in a file
    """
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
