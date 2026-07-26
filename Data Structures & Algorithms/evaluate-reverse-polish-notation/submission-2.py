class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isnumeric():
                stack.append(int(t))
            else:
                # pull the numbers from stack
                # and perform the operation
                result = stack.pop() # get the first operand
                if t == "+":
                    while len(stack) > 0:
                        result += stack.pop()
                if t == "-":
                    while len(stack) > 0:
                        result = stack.pop() - result
                if t == "*":
                    while len(stack) > 0:
                        result *= stack.pop()
                if t == "/":
                    while len(stack) > 0:
                        result = stack.pop() // result
                stack.append(result)
            print(f"{stack=}")
        # final result would be the only item in the stack
        return stack.pop()