class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        output = 0
        l, r = 0, len(height) - 1 # Left & right pointer at each side to maximze width.
        
        while l < r:
            area = (r - l) * min(height[l], height[r]) # Area = the smaller side * width
            output = max(output, area)
            
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
                
        return output
        
'''
Time: O(n)
Space: O(1)
'''
