class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        record = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for i in s:
            if i in record:
                if stack and stack[-1] == record[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if stack == [] else False
      
'''
Time: O(n)
Space: O(n)
'''
