class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            alphas = [0]*26
            for c in s:
                alphas[ord(c)-ord('a')] = alphas[ord(c)-ord('a')] + 1
            for c in t:
                alphas[ord(c)-ord('a')] = alphas[ord(c)-ord('a')] - 1

            for i in alphas:
                if i != 0:
                    return False
            return True
        anaGrps = []
        l = len(strs)
        taken = [0]*l
        for i in range(l):
            if taken[i] != 1:
                anaa = [strs[i]]
                taken[i] = 1
                for j in range(i+1, l):
                    if isAnagram(strs[i], strs[j]):
                        anaa.append(strs[j])
                        taken[j] = 1
                anaGrps.append(anaa)
        return anaGrps