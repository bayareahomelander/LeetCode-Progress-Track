class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for char, word in zip(pattern, words):
            if char in charToWord and charToWord[char] != w:
                return False
            if word in wordToChar and wordToChar[w] != char:
                return False
            
            charToWord[char] = word
            wordToChar[word] = char
        
        return True

'''
Time: O(n)
Space: O(n + m)
'''
