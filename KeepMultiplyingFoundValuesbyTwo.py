class Solution:
    def findFinalValue(self, nums: [int], original: int) -> int:
        s=set(nums)
        while original in s:
            original*=2
        return original
        
        


if __name__ == "__main__":
    s = Solution()
    print(s.findFinalValue([5,3,6,1,12], 3))
