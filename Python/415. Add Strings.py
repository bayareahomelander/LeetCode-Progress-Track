class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.helper(num1) + self.helper(num2))
    
    def helper(self, s):
        nums = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        output = 0
        
        for i in s:
            output = output * 10 + nums[i]
        
        return output

'''
Time: O(n)
Space: O(n)
'''
