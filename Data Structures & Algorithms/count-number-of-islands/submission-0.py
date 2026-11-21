class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])

        def recurse(row, col):
            if 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == "1":
                grid[row][col] = "0"
                recurse(row + 1, col)
                recurse(row, col + 1)
                recurse(row - 1, col)
                recurse(row, col - 1)
                return True

            return False

        count = 0
        for row in range(row_len):
            for col in range(col_len):
                if recurse(row, col):
                    count += 1
        
        return count
                    
