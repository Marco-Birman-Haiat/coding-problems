def productExceptSelf(nums: list[int]) -> list[int]:
    ans = []
    zeros = 0
    any_zero = False
    total_product_nz = 1

    for n in nums:
        total_product_nz = total_product_nz * n if n else total_product_nz
        zeros += 1 if not n else 0
    
    any_zero = zeros > 0

    if zeros >= 2:
        return [0 for _ in nums]
    for n in nums:
        if any_zero and n:
            ans.append(0)
        elif any_zero and not n:
            ans.append(int(total_product_nz))
        else:
            ans.append(int(total_product_nz / n))
    
    return ans

if __name__ == '__main__':
    print('tests')
    print(productExceptSelf([1,2,3,4]) == [24,12,8,6])
    print(productExceptSelf([1,-1,0,-3,3]) == [0,0,9,0,0])