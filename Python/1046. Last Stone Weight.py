class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort(reverse = True) # Make sure the first two elements are always the two heaviest stones.
        
        while True:
            if stones:
                if len(stones) == 1:
                    return stones[0]
                else:
                    if stones[0] == stones[1]:
                        stones = stones[2:]
                    else:
                        stones.append(stones[0] - stones[1])
                        stones = stones[2:]
                        stones.sort(reverse = True)
            else:
                return 0 # All stones smashed, none left.
                
'''
Time: O(nlogn)
Space: O(1)
'''
