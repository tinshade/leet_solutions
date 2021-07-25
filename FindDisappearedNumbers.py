class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        curated = set(range(1, n + 1))
        for num in nums:
            if num in curated:
                curated.remove(num)
        return list(curated)


s = Solution()
arr1 = [4,3,2,7,8,2,3,1] #5,6
arr2 = [1,1] #2
print(s.findDisappearedNumbers(arr1))
print(s.findDisappearedNumbers(arr2))
