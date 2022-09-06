class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = self.sumOf(n)
            
            if n == 1:
                return True
        
        return False
        
    def sumOf(self, n: int) -> int:
        output = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
            
        return output
   
'''
Time: O(1)
Space: O(n)
'''
        
