def is_subsequence(s: str, t: str) -> bool:
      c = 0
      i = 0
      if not len(s):
          return True
      while c < len(s) and i < len(t):
          if s[c] == t[i]:
              c+=1
          i+=1
      
      return c == len(s)

if __name__ == '__main__':
    print('tests')
    print(is_subsequence('abc', 'ahbgcd') == True)
    print(is_subsequence('axc', 'ahbcxd') == False)