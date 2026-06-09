class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                char_a, char_b = stack.pop(), stack.pop()
                stack.append(char_b - char_a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                char_a, char_b = stack.pop(), stack.pop()
                stack.append(int(char_b/char_a))
            else:
                stack.append(int(char))

        return stack[0]