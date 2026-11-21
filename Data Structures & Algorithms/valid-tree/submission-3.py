class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque
        if len(edges) != n - 1:
            return False

        dp = [[] for _ in range(n)]
    
        for e in edges:
            dp[e[0]].append(e[1])
            dp[e[1]].append(e[0])
        
        visited = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for neig in dp[node]:
                if neig not in visited:
                    visited.add(neig)
                    q.append(neig)

        return len(visited) == n
