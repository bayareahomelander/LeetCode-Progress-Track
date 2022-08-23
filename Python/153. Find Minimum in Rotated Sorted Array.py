class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l+r) // 2
            
            if nums[mid] > nums[r]: # Compare mid with the rightmost value, if greater then array must've been rotated.
                l = mid+1
                
            else: # Else array may be sorted in ascending order, move right pointer to midpoint.
                r = mid
                
        return nums[l]

'''
Time: O(logN)
Space: O(1)
'''
