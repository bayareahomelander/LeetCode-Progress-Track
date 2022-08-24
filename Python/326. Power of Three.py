class Solution:
    def isPowerOfThree(self, n: int) -> bool: # Option 1
        
        if n == 1:
            return True
        
        if n < 3 or n % 2 == 0: # n is even or less than 3.
            return False
        
        while n % 3 == 0: # Keep dividing n by 3.
            n //= 3
            
        return n == 1 # Check if current value is 1.
                      # e.g. 21 -> 7 != 1, therefore 21 is not power of 3.
                      # e.g. 27 -> 9 -> 3 -> 1 == 1.

'''
Time: O(n)
Space: O(1)
'''
    def isPowerOfThree(self, n: int) -> bool: # Option 2
        
        return 1162261467 % n == 0 # Largest power of 3 value possible under 32-bit.
      
'''
Time: O(1)
Space: O(1)
'''
