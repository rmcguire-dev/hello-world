# python 3


def gcd(a, b):
    c = 1
    while c != 0:
        c = a % b
        a, b = b, c
    return a


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))
