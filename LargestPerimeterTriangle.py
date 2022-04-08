class Solution:
    def largestPerimeter(self, nums) -> int:
        nums = sorted(nums,reverse=True)
        for x,y,z in zip(nums,nums[1:], nums[2:]):
            if y + z > x:
                return y + z + x
        return 0
s = Solution()
print(s.largestPerimeter([2,1,2]))
print(s.largestPerimeter([1,2,1]))