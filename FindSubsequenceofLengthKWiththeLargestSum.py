class Solution:
    def maxSubsequence(self, nums: [int], k: int) -> [int]:
        end = 0+k
        start = 0
        curr_max = 0
        while end <= len(nums):
            temp = nums[start:end]
            curr_max = max(curr_max, sum(temp))
            #print(temp, curr_max)
            start += 1
            end += k
        
        return nums[start:end]


if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3,3]
    k = 2
    print(s.maxSubsequence(nums, k)) # [3,3]

    nums = [-1,-2,3,4]
    k = 3
    print(s.maxSubsequence(nums, k)) # [-1,3,4]

    nums = [3,4,3,3]
    k = 2
    print(s.maxSubsequence(nums, k)) # [3,4]