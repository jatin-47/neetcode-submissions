class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        for n in values:
            if n-1 not in values:
                length = 1
                while n + length in values:
                    length += 1

                longest = max(length, longest)
        return longest