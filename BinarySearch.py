import time
class Solution:
	def naiveApproach(self, nums, target):
		print("NAIVE APPROACH")
		start_timer = time.perf_counter()
		for i in range(len(nums)):
			if nums[i] == target:
				end_timer = time.perf_counter()
				print(f"Time Taken : {end_timer - start_timer}s")
				return i
		end_timer = time.perf_counter()
		print(f"Time Taken : {end_timer - start_timer}s")
		return -1
	def search(self, nums, target):
		print("BINARY SEARCH APPROACH")
		start_timer = time.perf_counter()
		start, mid, end = 0, 0, len(nums)-1
		while start <= end:
			mid = (end+start)//2
			if target == nums[mid]:
				end_timer = time.perf_counter()
				print(f"Time Taken : {end_timer - start_timer}s")
				return mid #Over the iterations, if target exists, mid will once have the target value
			elif target > nums[mid]:
				#Target lies on the second half
				start = mid + 1 #Ignore the left half
			elif target < nums[mid]:
				#Target lies in the first half
				end = mid - 1 #Ignore the right half
		end_timer = time.perf_counter()
		print(f"Time Taken : {end_timer - start_timer}s")
		print(start,mid,end)
		return -1 #Target element was never found

s = Solution()
print(s.naiveApproach([-1,0,3,4,9,12],9)) #4
print(s.search([-1,0,3,4,9,12],9)) #4
print(s.search([1,3,5,6],5)) #2