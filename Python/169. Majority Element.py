class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        threshold = len(nums) / 2
        seen = {}
        
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        
        for k, v in seen.items():
            if v > threshold:
                return k

'''
Time: O(n)
Space: O(n)
'''
