# python 3


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        c = 1
        d = a*b
        while c != 0:
            c = a % b
            a, b = b, c
    return int(d/a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
