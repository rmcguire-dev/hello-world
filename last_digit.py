""" Last Digit of a Large Fibonacci Number
 Given an integer π, find the last digit of the πth Fibonacci number πΉπ (that is, πΉπ mod 10).

 Specification
 Input: The input consists of a single integer n.
 Constraints: 0 β€ π β€ 10^7
 Output: Output the last digit of πΉπ.

 Samples
 >>> n = 3
 >>> last_digit(n)
 >>> 2
 >>> πΉ3 = 2.
 >>> # Explanation: the third digit is 2 and this is the only digit and therefore the last.
 >>> n = 331
 >>> last_digit(n)
 9
 >>> # Explanation: The last digit of the three hundredth and thirty first digit is 9.
 >>> # πΉ331 = 668996615388005031531000081241745415306766517246774551964595292186469."""


def last_digit(n):
    if n == 0:
        return 0
    else:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append((f[i - 2] + f[i - 1]) % 10)
        return f[-1]


n = int(input())
print(last_digit(n))
