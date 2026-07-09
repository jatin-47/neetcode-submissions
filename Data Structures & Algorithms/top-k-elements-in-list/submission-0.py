class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        sorte = sorted(count.items(), key= lambda item : item[1], reverse=True)

        return [sorte[i][0] for i in range(k)]