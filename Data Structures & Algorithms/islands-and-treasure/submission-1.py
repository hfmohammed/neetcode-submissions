class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        row_len, col_len = len(grid), len(grid[0])


        q = deque()
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 0:
                    q.append((row, col))

          
        cost = 0
        offset = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in offset:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = cost + 1
                        q.append((nr, nc))

            cost += 1



                
