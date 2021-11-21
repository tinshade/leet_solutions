class Solution:
	def sortedListVariant(self, arr):
		#Iff the list was sorted, this would be the best solution
		smallest=1 #1 is the smallest positive integer by logic
		for i in range(len(arr)):
			if arr[i] == smallest:
				smallest+=1
		return smallest
	def firstMissingPositive(self, arr):
		n = len(arr)
		for i in range(n):
			#If the iTh element is negative, change it to zero
			if arr[i] < 0:
				arr[i] = 0
		for i in range(n):
			#Change values to negative when the values are in-bound
			val = abs(arr[i])

			#Checking if the value is in bounds and greater than zero, if it is, change the value to its negation
			if 1 <= arr[i] < n:
				if arr[i] > 0:
					arr[val-1] *= -1
				#If the value happens to be a zero, change it to an out-of-bounds value
				elif arr[i] == 0:
					#Doesn't matter if there are multiple -999s since the target is either within 1-len(arr) or is len(arr) and has to be positive
					arr[val-1] = -999
				else:
					pass

		# Final iteration over the same input array to check for the smallest positive integer
		# The target will belong to 1,len(arr)-1, if not, then it is len(arr), i.e. [1,2,3,4] => 5
		for i in range(1, n+1):
			if arr[i-1] >= 0:
				return i
		return n

	def cyclicSort(self, nums):
		i = 0
		if len(nums) == 1 and nums[0] == 1:
			return 2
		while i < len(nums):
			correct = nums[i]-1
			if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[correct]:
				i+=1
			else:
				nums[i], nums[correct] = nums[correct], nums[i]

		for i in range(len(nums)):
			if nums[i] != i+1:
				return i+1
		return len(nums)


	def workingSolution(self, nums):
		nums = set(nums)
		num = 1
		while num in nums:
			num += 1
		return num





s = Solution()
#Sorted List Variant
#print(s.sortedListVariant([0,1,3,4])) #2
#print(s.sortedListVariant([0,1,2,3])) #4

#Unsorted List Variant
print(s.firstMissingPositive([3,0,6,-3])) #1
print(s.firstMissingPositive([7,8,9,11,12])) #1
print(s.firstMissingPositive([3,4,-1,1])) #2
print(s.firstMissingPositive([1,2,0])) #3
print(s.firstMissingPositive([1])) #2
print(s.firstMissingPositive([1,1])) #2


