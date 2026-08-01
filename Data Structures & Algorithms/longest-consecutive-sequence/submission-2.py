class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        checked_seq = {}
        def get_samllest_item(n):
            val = n
            while val in values:
                val -= 1
            return val+1

        for n in nums:
            already_done = False
            for item in checked_seq:
                if checked_seq[item][0] <= n <= checked_seq[item][1]:
                    already_done = True
                    break
            if already_done:
                continue

            start = get_samllest_item(n)

            val = start
            while val in values:
                val += 1

            checked_seq[val - start] = [start, val-1]

        return max(checked_seq.keys()) if checked_seq.keys() else 0




        