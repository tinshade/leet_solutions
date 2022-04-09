import functools
class Solution:
    def arraySign(self, nums) -> int:
        result = functools.reduce(lambda product,y:product*y, nums)
        if result > 0:
            return 1
        elif result < 0:
            return -1
        return 0



s = Solution()
print(s.arraySign([-1,-2,-3,-4,3,2,1])) #1
print(s.arraySign([1,5,0,2,-3])) #0