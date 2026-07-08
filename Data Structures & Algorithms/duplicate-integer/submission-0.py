class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            j = hashmap.get(i, None)
            if j is None:
                hashmap[i] = 1
            else:
                return True
        return False