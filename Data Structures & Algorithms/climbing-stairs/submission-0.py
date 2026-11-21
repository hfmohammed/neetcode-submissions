class Solution:
    def climbStairs(self, n: int) -> int:
        l = []
        c = 0
        
        for c in range(n + 1):
            if c >= 2:
                l.append(l[c-2] + l[c- 1])
            else:
                l.append(1)
        
        return l[-1]