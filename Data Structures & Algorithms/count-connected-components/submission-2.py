class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        all_nodes = set(i for i in range(n))
        dp = [[] for _ in range(n)]

        for u, v in edges:
            dp[u].append(v) 
            dp[v].append(u)

        count = 0
        while all_nodes:
            start = next(iter(all_nodes))
            q = deque([start])
            all_nodes.remove(start)
            while q:
                k = q.popleft()
                for i in dp[k]:
                    if i in all_nodes:
                        all_nodes.remove(i)
                        q.append(i)

            count += 1

        return count
