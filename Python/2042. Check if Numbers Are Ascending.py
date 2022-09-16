class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        temp = [int(i) for i in s.split() if i.isdigit() == True]
        
        for i in range(len(temp) - 1):
            if temp[i] >= temp[i+1]:
                return False
        
        return True
    
'''
Time: O(n)
Space: O(n)
'''
