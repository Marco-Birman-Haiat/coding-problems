def removeStars(s: str) -> str:
    stack = []
    for l in s:
        if l != '*':
            stack.append(l)
        else:
            stack.pop()
    
    return ''.join(stack)

if __name__ == '__main__':
    print('tests')
    print(removeStars("leet**cod*e") == "leetcode")
    print(removeStars("erase*****") == "erase")