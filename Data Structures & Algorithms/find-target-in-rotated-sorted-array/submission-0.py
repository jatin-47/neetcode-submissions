class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(target, nums, indxArr):
            # 5,6,1,2,3 - nums
            # 0,1,2,3,4 - indices
            # 2,3,4,0,1 - indxArr
            idx = -1
            l, r = 0, len(indxArr) - 1

            while l < r:
                m = (l+r)//2
                if nums[indxArr[m]] < target:
                    l = m + 1
                elif nums[indxArr[m]] > target:
                    r = m - 1
                else:
                    return indxArr[m]
            return idx

        l, r = 0, len(nums) - 1
        minIndx = -1
        flag = False
        while l < r:
            m = (l+r)//2
            if nums[l] < nums[m] < nums[r]:
                minIndx = l
                flag = True
                break
            if nums[l] > nums[m]:
                if l == m-1:
                    minIndx = m
                    flag = True
                    break
                r = m - 1
            else:
                l = m + 1

        if flag == False:
            minIndx = l

        indxArr = [0]* len(nums)

        i = minIndx
        idx = 0
        while i < len(nums):
            indxArr[idx] = i
            i += 1
            idx += 1

        i = 0
        while idx < len(nums):
            indxArr[idx] = i
            i += 1
            idx += 1

        print(minIndx, nums, indxArr)
        return binarySearch(target, nums, indxArr)
    