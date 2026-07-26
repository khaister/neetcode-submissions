import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(f"{t=}")
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                # pull 2 numbers from stack
                # and perform the operation
                b = stack.pop()
                a = stack.pop()
                
                result = None
                if t == "+":
                    result = a + b
                if t == "-":
                    result = a - b
                if t == "*":
                    result = a * b
                if t == "/":
                    result = int(a / b)

                # push result back to the stack for next operation if any
                stack.append(result)

        # final result would be the only item in the stack
        return stack.pop()
