class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for key, v in enumerate(nums):
            if v in seen and key - seen[v] <= k:
                return True
            
            seen[v] = key
        
        return False
            
'''
Time: O(n)
Space: O(n)
'''
