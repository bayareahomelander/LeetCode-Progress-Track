class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        counter = 0
        s = s.rstrip(' ')
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                counter += 1
            else:
                break
        
        return counter

'''
Time: O(n)
Space: O(1)
'''
