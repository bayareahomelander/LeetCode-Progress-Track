class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if 1 not in nums: # Smallest positive integer, base case. 
            return 1
        
        nums.sort()
        l = 0
        
        for r in range(1, len(nums)):
        
            # Three condition must be met:
            #   1. Difference not equal to 1 -> [1,3];
            #   2. The smaller number cannot be negative -> [-1, 1];
            #   3. The pair cannot have equal values -> [2,2]
            
            if nums[r] - 1 != nums[l] and nums[l] > 0 and nums[l] != nums[r]:
                return (nums[l] + 1)
            
            else: # Else, simply increment left pointer by 1, make sure left is always 1 less than right.
                l += 1
        
        return (nums[-1] + 1)

'''
Time: O(n)
Space: O(1) -> Sorting happens within the original array.
'''
