class Solution:
    def isValid(self, s: str) -> bool:

        def get_compliment(b):
            if b == '(':
                return ')'
            if b == '{':
                return '}'
            if b == '[':
                return ']'

        stack = deque()

        for b in s:
            if len(stack) > 0 and b == get_compliment(stack[-1]):
                stack.pop()
            else:
                stack.append(b)

        return True if len(stack) == 0 else False
        