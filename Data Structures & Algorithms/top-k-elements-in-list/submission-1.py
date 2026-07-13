class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # number : count
        # O(n)
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        # freq[count] = [number1, number2, ...]
        # O(n)
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for cnt in range(len(freq)-1, 0, -1):
            if len(freq[cnt]) != 0:
                for n in freq[cnt]:
                    res.append(n)
                    if len(res) == k:
                        return res