class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        record = set() # Using set for faster operation -> O(1)
        
        for i in nums:
            if i in record:
                return i
            else:
                record.add(i)
                
'''
Time: O(n)
Space: O(n)
'''
