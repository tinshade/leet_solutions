class Solution:
	def searchInsert(self, nums, target):
		start,mid,end = 0,0,len(nums)-1

		while start<=end:
			mid = (end+start)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				end = mid-1
			elif nums[mid] < target:
				start = mid + 1
		return start


s = Solution()
print(s.searchInsert([1,3,5,6],5)) #2
print(s.searchInsert([1,3,5,6],2)) #1
print(s.searchInsert([1,3,5,6],0)) #0
print(s.searchInsert([1,3,5,6],7)) #4
print(s.searchInsert([1],0)) #0