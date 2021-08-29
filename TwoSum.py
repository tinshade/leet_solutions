class Solution:
	def twoSum(self, nums, target):
		watched=dict()
		for i in range(len(nums)):
			if target-nums[i] in watched:
				return [watched[target-nums[i]],i]
			watched[nums[i]] = i



s = Solution()
print(s.twoSum([2,8,12,16], 20)) #[1,2]
print(s.twoSum([2,7,12,16], 9)) #[0,1]
