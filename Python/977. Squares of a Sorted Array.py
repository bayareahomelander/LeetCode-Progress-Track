class Solution: # One liner using sorted()
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])

'''
Time: O(nlogn)
Space: O(n)
'''

class Solution: # Two pointer
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        output = [None] * len(nums)
        l, r = 0, len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                output[i] = nums[l] ** 2
                l += 1
            else:
                output[i] = nums[r] ** 2
                r -= 1
        
        return output
     
'''
Time: O(n)
Space: O(n)
'''
