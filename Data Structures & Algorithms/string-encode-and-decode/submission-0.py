class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        # 5#jatin5#saini

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            result.append(s[i+1 : i + 1 + int(length)])
            i += int(length) + 1
        return result
            