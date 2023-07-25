def maxOperations(nums: list[int], k: int) -> int:
    removals = 0
    diffs = dict()

    for num in nums:
        diff = k - num
        if num in diffs and diffs[num] > 0:
            diffs[num] -= 1
            removals +=1
        elif diff in diffs:
            diffs[diff] +=1
        else:
            diffs[diff] = 1
        
        
    return removals

if __name__ == '__main__':
    print('tests')
    print(maxOperations([1,2,3,4], 5) == 2)
    print(maxOperations([3,1,3,4,3], 6) == 1)