class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                char_a, char_b = stack.pop(), stack.pop()
                stack.append(char_a - char_b)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                char_a, char_b = stack.pop(), stack.pop()
                stack.append(int(char_a / char_b))
            else:
                stack.append(int(char))

        return stack[0]