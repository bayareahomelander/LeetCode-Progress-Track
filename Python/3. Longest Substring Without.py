class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        record = [] # Empty array to keep track of unique characters.
        
        for i in s:
            while i in record:
                record.pop(0) # If a letter is already in the array, remove the leftmost character until no duplicates.
             
            record.append(i) # Else simply add the character.
            output = max(output, len(record)) # Constantly update the maximum value
        
        return output

'''
Time: O(n)
Space: O(n)
'''
