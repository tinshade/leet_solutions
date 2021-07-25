class Solution:
	def findMaxConsecutiveOnes(self, nums):

		#With Array
		'''
		results = []
		curr_max = 0
		n = len(nums)
		for i in range(n):
			if nums[i] == 1:
				curr_max +=1
			else:
				results.append(curr_max)
				curr_max = 0
		results.append(curr_max)
		return max(results)
		'''
		#Without array
		
		max_cons, curr_max = 0,0
		n = len(nums)
		for i in range(n):
			if nums[i] == 1:
				curr_max +=1
			else:
				if max_cons<curr_max:
					max_cons = curr_max
				curr_max = 0
		if max_cons<curr_max:
			max_cons = curr_max
		return max_cons

s = Solution()
nums1 =[1,1,0,1,1,1]
nums2 =[1,0,1,1,0,1]
print(s.findMaxConsecutiveOnes(nums2))

