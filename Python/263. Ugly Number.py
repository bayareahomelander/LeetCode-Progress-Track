class Solution:
    def isUgly(self, n: int) -> bool: # Bruce Force, won't pass but it works
        if n <= 0:
            return False
        if n == 1:
            return True
        
        factors = [i for i in range(1, n+1) if n % i == 0]
        ugly = [2,3,5]
        
        for i in factors[1:]:
            if self.isPrime(i) and i not in ugly:
                return False
        
        return True
        
    def isPrime(self, n):
        base = 2
        while base <= math.sqrt(n):
            if n % base < 1:
                return False
            else:
                base += 1
        return n > 1

class Solution:
  def isUgly(self, n: int) -> bool:
    if n <= 0:
      return False
    
    factors = [2,3,5]
    
    for i in factors:
      while n % i == 0:
        n //= i

    return n == 1 # If n can be reduced down to 1 then it is an ugly number
  
'''
Time: O(log2n)
Space: O(1)
'''
