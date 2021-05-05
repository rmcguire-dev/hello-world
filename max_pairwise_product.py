# python3

n = int(input())
a = [int(x) for x in input().split()]


a.sort()
product = a[-2] * a[-1]
print(product)
