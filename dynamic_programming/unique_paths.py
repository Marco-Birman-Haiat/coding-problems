import math

def uniquePaths(m: int, n: int) -> int:
    return int(math.factorial(m+n-2) / (math.factorial(n-1) * math.factorial(m-1)))

if __name__ == '__main__':
    print('tests')
    print(uniquePaths(3,7) == 28)
    print(uniquePaths(2,3) == 3)