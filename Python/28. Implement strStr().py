class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        if len(haystack) == len(needle): # Edge case.
            return 0
        
        l, r = 0, len(needle) # Sliding window with size of needle.
        
        while r <= len(haystack):
            if haystack[l:r] == needle: # Return the left pointer if current portion of haystack is equal to needle.
                return l
            else: # Else, shift the window to right by 1.
                l += 1
                r += 1
                
'''
Time: O(n)
Space: O(1)
'''
