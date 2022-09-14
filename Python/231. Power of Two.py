class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True 
        
        base = 2
        
        while base != n:
            if base > n:
                break
            else:
                base *= 2
        
        return base == n

'''
-> Brute Force
Time: O(n)
Space: O(1)
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      if n == 1:
        return True
      
      return n&(n-1) == 0 and n > 0
    
'''
-> Optimized Using Binary
Time: O(1)
Space: O(1)
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      
      if n == 1:
        return True
      
      if n < 1:
        return False
      
      return self.isPowerOfTwo(n/2)

'''
-> Recursion
Time: O(2^n)
Space: O(1)
'''
