class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == '':
            return t
        
        output = ''

        for i in set(t):
            if s.count(i) != t.count(i):
                output += i

        return output

'''
Time: O(n)
Space: O(1)
'''
