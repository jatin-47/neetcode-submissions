class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            min_ht = min(heights[i], heights[j])
            max_area = max((j-i)*min_ht, max_area)
            if min_ht == heights[i]:
                i+=1
            else:
                j-=1

        return max_area
