class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # this is very famously solved using Stacks (done in my undergrad too)
        stack = []
        operators = {'+', '-', '*', '/'}

        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                if item == '+':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2+val1)
                if item == '-':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2-val1)
                if item == '*':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2*val1)
                if item == '/':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(int(val2/val1))
        return stack.pop()