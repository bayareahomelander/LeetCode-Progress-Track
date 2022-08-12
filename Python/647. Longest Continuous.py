class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if len(nums) == 1: # Base case.
            return 1
        
        counter = 1 # Keep track of the current longest substring, initialized to 1.
        l = 0 # Left pointer, used with right pointer to check numbers in pairs.
        record = [] # Return the maximum value of the array as final output.
        
        for r in range(1, len(nums)):
            if nums[r] > nums[l]:
                counter += 1
                
            else:
                record.append(counter)
                counter = 1
            
            l += 1 # Constantly increment by 1 at the end of each iteration, make sure left is 1 less than right.
        
        record.append(counter)
        
        return max(record)

'''
Time: O(n) -> Each element visited at most twice.
Space: O(n) -> Extra array needed for solution.
'''
