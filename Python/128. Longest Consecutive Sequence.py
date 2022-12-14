class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # Converting Array to Set for a faster operation.
        longestSeq = 0 # Initializing final output to 0.
        
        for i in nums:
            if (i - 1) not in nums: # Checking if the number has a left neighbor -> if not then it would be the start of a sequence.
                seqLength = 0 # Initializing temporary sequence length.
                
                while (i + seqLength) in nums:
                    seqLength += 1 # Incrementing seqLength by 1 everytime to check for right neighbors.
                    
                longestSeq = max(seqLength, longestSeq) # Updating the output to maximum length.
        
        return longestSeq

'''
Time: O(n)
    -> Straightforward solution would be O(nlogn) because of sorting algorithms runtime. 

# Space: O(n)
'''
