class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count('1')
      
'''
Time: O(n)
Space: O(1)
'''
