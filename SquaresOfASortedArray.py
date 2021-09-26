class Solution:
    def sortedSquares(self, nums):
      start, end, temp_pointer = 0, len(nums)-1, len(nums)-1
      result = []+nums
      while start <= end:
        if abs(nums[start]) > abs(nums[end]):
          result[temp_pointer] = nums[start]**2
          start += 1
        else:
          result[temp_pointer] = nums[end]**2
          end -= 1
        temp_pointer -=1
      return result



s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-5,-3,-2,-1]))
