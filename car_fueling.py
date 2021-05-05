# python 3


def compute_min_number_of_refills(d, m, n):
    count = -1
    current_fill = m
    for i in range(0, len(n) - 1):
        if n[i + 1] - n[i] > current_fill or d - n[-1] > current_fill:
            return -1
        current_amount = n[i] + n[i + 1]
        if current_amount < current_fill:
            current_fill = current_fill - current_amount
        else:
            count = count + 1
            current_fill = m
    return count


if __name__ == "__main__":
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n
