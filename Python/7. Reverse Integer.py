class Solution:
    def reverse(self, x: int) -> int: # String operation
        
        if len(str(x)) == 1: # Base case.
            return x
        
        output = None
        
        if x > 0:
            output = int(str(x)[::-1])
        
        elif x < 0: # If x is negative, multiply it by -1 to make it a positive int.
            x *= -1
            output = int('-' + str(x)[::-1])
        
        if output <= (-2)**31 or output >= (2**31) - 1: # Check for 64-bit integers.
            return 0
        
        return output

'''
Time: O(n)
Space: O(1)
'''

    def reverse(self, x: int) -> int: # Math approach
        
        output = 0
        
        while x != 0:
          if x < 0:
            x *= -1
          
          temp = x % 10
          output = output * 10 + temp
          x //= 10
        
        if x < 0:
          output *= -1
        
        if output <= (-2)**31 or output >= (2**31) - 1:
          return 0
        
        return output
