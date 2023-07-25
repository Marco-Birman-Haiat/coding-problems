from collections import deque

def decodeString(s: str) -> str:
    num_stack = []
    str_stack = []
    mult = 0

    for c in s:
        if c.isnumeric():
            num_stack.append(c)
        elif c == '[':
            nu = deque()
            str_stack.append(c)
            while len(num_stack) > 0 and type(num_stack[-1]) == str:
                nu.appendleft(num_stack.pop())
            num_stack.append(int(''.join(list(nu))))
        elif c != ']':
            str_stack.append(c)
        else:
            le = deque()
            while str_stack[-1] != '[':
                le.appendleft(str_stack.pop())
            
            str_stack.pop()
            
            word = list(le)
            mult = num_stack.pop()
            rep = word * mult
            str_stack.extend(rep)
            
    return ''.join(str_stack)

if __name__ == '__main__':
    print('tests')
    print(decodeString("3[a]2[bc]") == "aaabcbc")
    print(decodeString("3[a2[c]]") == "accaccacc")
    print(decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")