class Solution:
    def reverseBits(self, n: int) -> int:
        
        biString = '{0:032b}'.format(n)[::-1]
        
        return int(biString, 2)
        
'''
Time: O(n)
Space: O(1)
'''
