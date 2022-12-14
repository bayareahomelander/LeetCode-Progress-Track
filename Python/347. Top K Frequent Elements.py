class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {} # Creating an empty hashMap with key-value pairs being -> nums[i]:correspoding number of occurance
        
        if len(nums) == 1:
            return nums
        
        # If the number exists, increment its number of occurance by 1. Else, creat a key-value pair.
        for i in nums:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1
        
        # Creating a sorted array in descending order based on values, return the first K elements using Slicing.
        return sorted(record, key = record.get, reverse = True)[:k]

'''
Time: O(nlogn)
  -> For loop runtime: O(n) ignored since nlogn is greater than n.
Space: O(n)
'''
