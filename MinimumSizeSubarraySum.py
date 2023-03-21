class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        left, total = 0,0
        res = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right-left+1, res)
                total -= nums[left]
                left += 1

        
        return 0 if res == float('inf') else res

            



if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
    print(s.minSubArrayLen(4, [1,4,4])) # 1
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0
    print(s.minSubArrayLen(11, [1,2,3,4,5])) # 3
