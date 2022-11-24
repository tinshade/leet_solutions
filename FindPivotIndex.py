class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0 
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1
    


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6])) #3
print(s.pivotIndex([1,2,3])) #-1
print(s.pivotIndex([2,1,-1])) #0
