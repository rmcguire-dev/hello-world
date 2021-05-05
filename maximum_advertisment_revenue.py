# python 3

from itertools import permutations


def max_dot_product(a, b):
    my_array = []
    profit_per_click = sorted([i for i in a], reverse=True)
    average_number_of_clicks = sorted([j for j in b], reverse=True)
    for i in range(0, len(profit_per_click)):
        product = profit_per_click[i] * average_number_of_clicks[i]
        my_array.append(product)
    return sum(my_array)


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
