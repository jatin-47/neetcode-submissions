class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        num_zeroes = 0
        for n in nums:
            if n == 0:
                num_zeroes += 1
            else:
                total_product *= n
        
        if num_zeroes == 0:
            return [total_product//n for n in nums]
        if num_zeroes == 1:
            result = []
            for n in nums:
                if n == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            return result
        if num_zeroes > 1:
            return [0]*len(nums)

        