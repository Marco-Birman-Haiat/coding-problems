def asteroidCollision(asteroids: list[int]):
    stack = []

    for a in asteroids:
        if a > 0 or len(stack) == 0:
            stack.append(a)
        else:
            for _ in range(len(stack)):
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(a)
                    break
                elif abs(a) > stack[-1]:
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(a)
                        break
                elif abs(a) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
    return stack

if __name__ == '__main__':
    print('tests')
    print(asteroidCollision([5, 10, -5]) == [5, 10])
    print(asteroidCollision([8, -8]) == [])
    print(asteroidCollision([10, 2, -5]) == [10])