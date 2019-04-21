def knapsack(price, weight, rest, n):
    """
    solve 0/1 knapsack problem
    :param price: price
    :param weight: weight
    :param rest: total capacity
    :param n: used in recursion
    :return: maximum price
    """
    if rest == 0 or n == -1:
        return 0

    if weight[n] <= rest:
        return max(price[n] + knapsack(price, weight, rest -
            weight[n], n-1), knapsack(price, weight, rest, n-1))
    else:
        return knapsack(price, weight, rest, n-1)


def findMaxKnapsack(P,W,M):
    """
    solve partial knapsack problem
    :param P: price
    :param W: weight
    :param M: total capacity
    :return: X
    """
    ratio=[]
    X=[0 for i in range(len(P))]

    for i in range(len(P)):
        ratio.append(P[i]/W[i])

    # sort the ratio and its index in descending order
    # format: dR[i][0]=index, dR[i][1]=ratio
    descendingRatio = sorted(enumerate(ratio), key= lambda x: x[1], reverse=True)

    curr = 0
    while M > 0:
        maxIndexValue=descendingRatio[curr][0]

        if W[maxIndexValue] <= M:
            X[maxIndexValue] = 1
        else:
            X[maxIndexValue]=M/W[maxIndexValue]

        M -= W[maxIndexValue] * X[maxIndexValue]
        curr += 1

    # for i in range(len(X)):
    #     print("X", i, " :", X[i])

    return X

price = [60, 100, 120]
weight = [10, 20, 30]
X=[0, 0, 0]
rest = 50
n = len(price) - 1

print(knapsack(price, weight, rest, n))
print(findMaxKnapsack(price,weight,rest))