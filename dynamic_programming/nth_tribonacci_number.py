memo = {}
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return memo[n]

if __name__ == '__main__':
    print('tests')
    print(tribonacci(4) == 4)
    print(tribonacci(25) == 1389537)