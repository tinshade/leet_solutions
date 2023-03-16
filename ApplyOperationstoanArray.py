class Solution:
    def applyOperations(self, nums: [int]) -> [int]:
        n = len(nums)
        j = 0
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        
        if nums[n - 1] != 0:
            nums[j], nums[n - 1] = nums[n - 1], nums[j]
            j += 1
        
        for i in range(j, n):
            nums[i] = 0
        
        return nums






if __name__ == "__main__":
    s = Solution()
    print(s.applyOperations([1,2,2,1,1,0])) # [1,4,2,0,0,0]
    print(s.applyOperations([0,1])) # [1,0]