class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        curSum = sum(nums) # Sum of current array
        corSum = sum([i for i in range(1, len(nums) + 1)]) # Correct sum without duplicates
        noDup = sum(set(nums)) # Sum of current array without duplicates
        
        miss = corSum - noDup
        duplicate = curSum - noDup
        
        return [duplicate, miss]
      
'''
Time: O(n)
Space: O(1)
'''
