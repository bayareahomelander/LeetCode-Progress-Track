class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        perfect = {6, 28, 496, 8128, 33550336}
        
        return num in perfect
        
        
'''
Time: O(1)
Space: O(1)
'''
