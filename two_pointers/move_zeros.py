def moveZeroes(nums: list[int]) -> None:
    i = 0
    zc = 0
    while i < len(nums) and zc + i < len(nums):
        if nums[i] == 0:
            zero = nums.pop(i)
            nums.append(zero)
            zc+=1
        else:
            i += 1
    return nums

if __name__ == '__main__':
    print('tests')
    print(moveZeroes([0,1,0,3,12]) == [1,3,12,0,0])
    print(moveZeroes([0]) == [0])
    print(moveZeroes([0,0,1,0,10,7,0,0]) == [1,10,7,0,0,0,0,0])