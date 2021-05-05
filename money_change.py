# python 3


def get_change(m):
    count = 0
    while m > 0:
        if m % 10 == 0:
            count += 1
            m -= 10
        elif m % 5 == 0:
            count += 1
            m -= 5
        else:
            count += 1
            m -= 1
    return count


m = int(input())
print(get_change(m))
