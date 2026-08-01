class Solution:
    def isValid(self, s: str) -> bool:
        compliment_brak = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = deque()

        for b in s:
            if len(stack) > 0 and b == compliment_brak.get(stack[-1]):
                stack.pop()
            else:
                stack.append(b)

        return True if len(stack) == 0 else False
        