# python 3


def largest_number(numbers):
    if len(numbers) == 2:
        k = sorted([k for k in numbers])
        p = [str(i) for i in k]
        m = int("".join(p))
        return m
    v = sorted([j for j in numbers], reverse=True)
    s = [str(i) for i in v]
    res = int("".join(s))
    return res


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
