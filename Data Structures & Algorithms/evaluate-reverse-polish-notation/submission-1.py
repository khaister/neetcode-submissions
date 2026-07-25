class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isnumeric():
                stack.append(int(t))
            else:
                # pull the numbers from stack
                # and perform the operation
                result = 0
                if t == "+":
                    while len(stack) > 0:
                        result += stack.pop()
                if t == "-":
                    while len(stack) > 0:
                        result -= stack.pop()
                if t == "*":
                    result = 1  # need this so that we're not multiplying w/ zero
                    while len(stack) > 0:
                        result *= stack.pop()
                if t == "/":
                    while len(stack) > 0:
                        result //= stack.pop()
                stack.append(result)
        # final result would be the only item in the stack
        return stack.pop()