class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        if num // 10 == 0:
            return num
        
        while num // 10 != 0:
            num = self.helper(num)
        
        return num
            
            
    def helper(self, num):
        num = list(str(num))
        output = sum([int(i) for i in num])
        
        return output
      
'''
Time: O(n)
Space: O(n)
'''
