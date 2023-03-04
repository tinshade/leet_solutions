class Solution:
    def singleNonDuplicate(self, nums) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                return nums[i]
            
            i+=2
            j+=2
        return nums[-1]







if __name__ == "__main__":
    manager = Solution()
    print(manager.singleNonDuplicate([3,3,7,7,10,11,11])) # 10
    print(manager.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # 2
    print(manager.singleNonDuplicate([1])) # 1
    print(manager.singleNonDuplicate([1,1,2])) # 2