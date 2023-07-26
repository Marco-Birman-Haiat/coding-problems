def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if not len(flowerbed):
        return n <= 0
    
    if len(flowerbed) <= 2 and not any(flowerbed):
        return n - 1 <= 0
    
    for i in range(len(flowerbed)):
        if i == 0 and not any(flowerbed[:2]):
            flowerbed[i] = 1
            n-=1
        elif i > 0 and i < len(flowerbed) - 1 and not any(flowerbed[i-1:i+2]):
            flowerbed[i] = 1
            n-=1
        elif i == len(flowerbed) - 1 and not any(flowerbed[-2:]):
            flowerbed[i] = 1
            n-=1
        

    
    return n <= 0

if __name__ == '__main__':
    print('tests')
    print(canPlaceFlowers([1,0,0,0,1], 1) == True)
    print(canPlaceFlowers([1,0,0,0,1], 2) == False)