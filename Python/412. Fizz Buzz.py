class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        if n == 1:
            return ['1']
        
        fizz = ['1','2']
        
        for i in range(3, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizz.append('FizzBuzz')
            elif i % 5 == 0:
                fizz.append('Buzz')
            elif i % 3 == 0:
                fizz.append('Fizz')
            else:
                fizz.append(str(i))
        
        return fizz
      
'''
Time: O(n)
Space: O(n)
'''
