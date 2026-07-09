class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n1 = None
        n2 = None
        countingMap = {}
        new = []
        for i in nums:
            countingMap[i] = 1 + countingMap.get(i, 0)
            new.append(target-i)

        for idx, i in enumerate(new):
            if i in countingMap and nums[idx] != i:
                if n1 == None:
                    n1 = idx 
                elif n2 == None:
                    n2 = idx

        return sorted([n1, n2])



        