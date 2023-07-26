data = {}
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    if n in data:
        return data[n]

    data[n] = cost[-1] + min(minCostClimbingStairs(cost[:n-1]),
                minCostClimbingStairs(cost[:n-2]))

    return min(data[n], minCostClimbingStairs(cost[:n-1]))

if __name__ == '__main__':
    print('tests')
    print(minCostClimbingStairs([10, 15, 20]) == 15)
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6)