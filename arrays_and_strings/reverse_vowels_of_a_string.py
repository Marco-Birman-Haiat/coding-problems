vowels = ('a', 'e', 'i', 'o', 'u')
def reverseVowels(s: str) -> str:
    v = []
    sl = [l for l in s]
    for l in s:
        if l.lower() in vowels:
            v.append(l)
    
    for i in range(len(s)):
        if s[i].lower() in vowels:
            sl[i] = v.pop()
    return ''.join(sl)


if __name__ == '__main__':
    print('tests')
    print(reverseVowels("hello") == "holle")
    print(reverseVowels("AbcDEifgHo") == "obcDiEfgHA")