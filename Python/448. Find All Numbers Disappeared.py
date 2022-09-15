class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        temp = set([i for i in range(1, len(nums) + 1)])
        nums = set(nums)
        
        return list(temp - nums)
      
'''
Time: O(n)
Space: O(n)
'''
