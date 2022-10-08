/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let record = new Map();
  
  for (let i = 0; i < nums.length; i++) {
    if (record.has(target - nums[i])) {
      return [record.get(target - nums[i]), i];
    } else {
      record.set(nums[i], i)
    }
  }
    return [];
};

/*
Time: O(n)
Space: O(n)
*/
