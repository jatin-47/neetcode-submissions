class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 0
        one, two  = n, 0
        numerator = math.factorial(one+two)
        deno_one = numerator
        deno_two = 1
        while one >= 0:
            total_ways += numerator/(deno_one*deno_two)
            numerator /= (one + two)
            if one*(one-1) != 0:
                deno_one /= one*(one-1)
            deno_two *= (two+1)
            one -= 2
            two += 1
        print(total_ways)
        return math.ceil(total_ways)


        


        