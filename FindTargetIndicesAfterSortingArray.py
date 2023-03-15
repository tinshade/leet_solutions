class Solution:
    def targetIndices(self, nums, target: int):
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        
        return answer



if __name__ == "__main__":
    s = Solution()
    print(s.targetIndices([1,2,5,2,3], 2)) # [1,2]
    print(s.targetIndices([1,2,5,2,3], 3)) # [3]
    print(s.targetIndices([1,2,5,2,3], 5)) # [4]