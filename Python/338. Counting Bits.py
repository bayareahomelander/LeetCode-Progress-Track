class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = [0]
        
        for i in range(1, n+1):
            output.append(self.helper(i))
            
        return output
            
    
    def helper(self, n):
        m = str(int('{0:032b}'.format(n)))
        ones = m.count('1')
        
        return ones

'''
Time: O(n)
Space: O(n)
'''
