from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for l in s:
            if l != '*':
                stack.append(l)
            else:
                stack.pop()
        
        return ''.join(stack)