class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # Creating two pointers at the beginning and end of the array.
        
        while l < r:
            cur = numbers[l] + numbers[r]
            
            # If current sum is less than target, increment left pointer by 1;
            # Else if greater than target, decrement right pointer by 1;
            # If both conditions false then numbers have been found, return indexes.
            
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return [l+1, r+1]

'''
Time: O(n)
Space: O(1)
'''

# Intuition: Brute Force Solution
def twoSum(self, numbers: List[int], target: int) -> List[int]:
  for i in range(len(numbers)):
    for j in numbers[i:]:
      if numbers[i] + numbers[j] == target:
        return [i+1, j+1]

'''
Constant space but time is quadratic, worse case -> (array.length * each number in the array)
'''
