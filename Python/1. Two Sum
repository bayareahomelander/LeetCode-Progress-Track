class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {} # Creating a hashMap with key-value pairs being -> value:index

        for i, n in enumerate(nums):
            diff = target - n # Initializing the difference between target & n
            
            # If different exists in hashMap, return its index and the number's. Else, create a key-value pair.
            if diff in record:
                return [record[diff], i]
            record[n] = i

Time: O(n)
Space: O(n)
