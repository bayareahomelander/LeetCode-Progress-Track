class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    
        # Creating a hashMap for numbers 0 to 9 with corresponding value.
        record = {
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '0':0
        }
        
        # Two additional variable for the inputs.
        int1 = 0
        int2 = 0
        
        for i in num1:
            int1 = int1 * 10 + record[i]
        
        for i in num2:
            int2 = int2 * 10 + record[i]
            
        return str(int1*int2)
      
'''
Time: O(n)
Space: O(n)
'''
