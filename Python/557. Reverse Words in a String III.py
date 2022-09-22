class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        output = []
        
        for i in temp:
            i = i[::-1]
            output.append(i)
            
        return ' '.join(output)
      
'''
Time: O(n)
Space: O(1)
'''
