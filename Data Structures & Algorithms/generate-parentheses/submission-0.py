class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                print(stack)
                backtracking(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                print(stack)
                backtracking(open_count, close_count + 1)
                stack.pop()

        backtracking(0, 0)
        return res