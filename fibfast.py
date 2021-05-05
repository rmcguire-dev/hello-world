"""Fibonacci Number.
Given an integer n, find the nth Fibonacci number Fn.

Specification
Input: The input consists of a single integer n.
Constraints: 0 <= n <= 45.
Output Format: Output Fn

Samples
>>> n = 10
>>> fibonacci_fast(n)
55
>>> # Explanation: To achieve the value 55
>>> # take the 10th number of the sequence """


def fibonacci_fast(n):
    if n == 0:
        return 0
    else:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 2] + f[i - 1])
        return f[-1]


n = int(input())
print(fibonacci_fast(n))
