# python 3


"""Fractional Knapsack.
    Given a set of items and total capacity of a knapsack,
    find the maximal value of fractions of items that fit into the knapsack.
    Samples:
    >>> n = 3; capacity = 50; weights = [60, 100, 120]; values = [20, 50, 30]
    >>> get_optimal_value(capacity, weights, values)
    180.0000
    >>> # Explanation: To achieve the value 180, we take the first item and
    >>> # the third item into the bag.
    >>> n = 1; capacity = 10; weights = [500]; values = [30]
    166.6667
    >>> # Explanation: Here, we just take one third of the only available item.
    """


def knapsack(W, w, v):
    A, V = [0] * len(w), 0
    v = sorted([v / w for v, w in zip(v, w)], reverse=True)
    for i in range(0, len(A)):
        if W == 0:
            return V
        a = min(w[i], W)
        V = V + a * v[i]
        w[i] = w[i] - a
        A[i] = A[i] + a
        W = W - a
    return V


print(knapsack(50, [60, 100, 120], [20, 50, 30]))
# print(knapsack(10, [500], [30]))
