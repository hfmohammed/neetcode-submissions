class Solution:
    def isValid(self, l) -> bool:
        l_read = set()
        for i in l:
            if i == ".":
                continue

            if not (0 < int(i) < 10):
                print("constraint failed")
                return False

            if i in l_read:
                print(l)
                print(l_read)
                print("read i already")
                return False
            else:
                l_read.add(i)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for l in board:
            if not self.isValid(l):
                return False
        
        for i in range(9):
            v_temp_vert = []
            for j in range(9):
                v_temp_vert.append(board[j][i])

            if not self.isValid(v_temp_vert):
                return False
        
        for i in range(3):
            for j in range(3):
                v_temp_sub = []
                v_temp_sub += board[i * 3][j * 3 : j * 3 + 3]
                v_temp_sub += board[i * 3 + 1][j * 3 : j * 3 + 3]
                v_temp_sub += board[i * 3 + 2][j * 3 : j * 3 + 3]
                if not self.isValid(v_temp_sub):
                    return False
        
        return True