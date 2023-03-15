class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        answer = 0
        for i in range(1, len(nums), 2):
            answer += min(nums[i], nums[i-1])
        
        return answer




if __name__ == "__main__":
    s = Solution()
    print(s.arrayPairSum([1,4,3,2])) # 4
    print(s.arrayPairSum([6,2,6,5,1,2])) # 9