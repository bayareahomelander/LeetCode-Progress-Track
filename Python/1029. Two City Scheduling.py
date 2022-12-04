class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityA = sum([i[0] for i in costs]) # Send everyone to city A first and calculate the total
        diff = [(c2 - c1) for c1, c2 in costs] # If (c2 - c1) < 0: cost B is less than cost A -> reassign to city B
        diff.sort() # Make sure that the smallest values are in the front of list
        
        total = sum(diffs[:len(costs) // 2]) # Integer division to get the first half -> goal is to fly 2n/2 people to each city
        
        return cityA + total
      
'''
Time: O(nlogn)
Space: O(n)
'''
