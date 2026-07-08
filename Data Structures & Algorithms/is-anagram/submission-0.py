class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charHash = {}
        for char in s:
            if charHash.get(char, None) is None:
                charHash[char] = 1
            else:
                charHash[char] = charHash[char] + 1
        for char in t:
            if charHash.get(char, None) is None:
                return False
            else:
                charHash[char] = charHash[char] - 1
        
        for char, count in charHash.items():
            if count != 0:
                return False
        return True