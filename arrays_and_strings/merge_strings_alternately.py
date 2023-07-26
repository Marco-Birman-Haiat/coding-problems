def mergeAlternately(word1: str, word2: str) -> str:
    result = ''
    
    for index in range(max(len(word1), len(word2))):
        if index < len(word1):
            result += word1[index]
        
        if index < len(word2):
            result += word2[index]

    return result

if __name__ == '__main__':
    print('tests')
    print(mergeAlternately('abcd', 'pq') == 'apbqcd')
    print(mergeAlternately('abc', 'pqr') == 'apbqcr')