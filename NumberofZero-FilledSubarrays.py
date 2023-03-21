class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] == 0:
            return 1
        
        index, counter = 0, 0

        while index < n:
            count = 0
            while index < n and nums[index] == 0:
                count += 1
                index += 1
                counter += count
            index += 1
        
        return counter


if __name__ == "__main__":
    s = Solution()
    print(s.zeroFilledSubarray([1,3,0,0,2,0,0,4])) # 6
    print(s.zeroFilledSubarray([0,0,0,2,0,0])) # 9
    print(s.zeroFilledSubarray([2,10,2019])) # 0