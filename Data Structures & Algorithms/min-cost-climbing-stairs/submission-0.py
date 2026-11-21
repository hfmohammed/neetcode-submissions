class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up
        cost.append(0)
        l = []
        for i in range(len(cost)):
            if i == 0 or i == 1:
                l.append(cost[i])
            else:
                l.append(cost[i] + min(l[i - 1], l[i - 2])) 

        return l[-1]