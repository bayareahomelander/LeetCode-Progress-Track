class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == ' ' or len(s) == 1: # Base cases.
            return True
            
        # Creating a new string that is without non-alphanumeric characters and in lowercase.
        temp = ''.join([i for i in s if i.isalnum()]).lower()
        
        return temp == temp[::-1]

Time Complexity: O(n)
Space Complexity: O(n)
