class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        if digits == '':
            return []
        
        if len(digits) == 1:
            return list(letters[digits])
        
        temp = ['']
        
        for i in digits:
            temp = [p + q for p in temp for q in letters[i]]
        
        return temp
      
'''
Time: O(2^n)
Space: O(n)
'''
