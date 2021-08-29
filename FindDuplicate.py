class Solution:
		def findDuplicate(self, nums):
			slow = nums[0]
			fast = nums[slow]
			while fast != slow:
				slow = nums[slow]
				fast = nums[nums[fast]]

			slow = 0
			while slow != fast:
				slow = nums[slow]
				fast = nums[fast]
			return slow


		def findDuplicatePythonic(self, nums):
			from collections import Counter
			for key, value in Counter(nums).items():
				if value == 2:
					return key

s = Solution()
print(s.findDuplicate([1,3,4,2,2]), s.findDuplicatePythonic([1,3,4,2,2])) #2