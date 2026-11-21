class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        idx = 0

        while idx < len(tokens):
            if tokens[idx] not in ['+', '-', '/', '*']:
                a = int(tokens[idx])
                stack.append(a)

            else:
                b = stack.pop()
                a = stack.pop()
                op = tokens[idx]
                
                if op == "+":
                    c = a + b

                elif op == "-":
                    c = a - b

                elif op == "/":
                    c = int(a / b)

                elif op == "*":
                    c = a * b
                
                stack.append(c)
            
            print(stack)
            idx += 1

        return stack[0]
        