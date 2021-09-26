class Solution:
def moveZeroes(self, nums):
  zero_count = nums.count(0)
  next_non_zero = 0
  for n in nums :
    if n != 0 :
      nums [next_non_zero] = n
      next_non_zero += 1
  for zero in range(1, zero_count + 1):
    nums [-zero] = 0

def pythonic(self, nums):
  i, zeroes = 0,0
  while i<len(nums):
      if nums[i] == 0:
          zeroes +=1
          del nums[i]
      else:
          i += 1
  for z in range(zeroes):
      nums.append(0)

s = Solution()
s.moveZeroes([0,1,0,3,12])