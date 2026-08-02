class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 0
        one, two  = n, 0
        while one >= 0:
            total_ways += math.factorial(one+two)/(math.factorial(one)*math.factorial(two))
            one -= 2
            two += 1

        return int(total_ways)


        


        