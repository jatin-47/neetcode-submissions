class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []
        alphanumerics = [chr(ord('a')+i) for i in range(26)] + [str(i) for i in range(10)]
        for c in s:
            if c.lower() in alphanumerics:
                r.append(c.lower())

        cleaned = "".join(r)

        i = 0
        j = len(cleaned) - 1

        while i < j:
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True