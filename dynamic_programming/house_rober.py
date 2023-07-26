def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    money = [0 for _ in nums]
    money[0] = nums[0]
    money[1] = nums[1]

    for i in range(2, len(nums)):
        money[i] = nums[i] + max(money[:i-1])
    
    return max(money[-1], money[-2])

if __name__ == '__main__':
    print('tests')
    print(rob([1,2,3,1]) == 4)
    print(rob([2,7,9,3,1]) == 12)