class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        threshold = len(nums) / 3
        output = []
        seen = {}
        
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        
        for i in seen:
            if seen[i] > threshold:
                output.append(i)
        
        return output
      
'''
Time: O(n)
Space: O(1)
'''
