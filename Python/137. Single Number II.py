class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        
        nums.sort(key = Counter(nums).get)
        return nums[0]
      
'''
Time: O(n)
Space: O(1)
'''
