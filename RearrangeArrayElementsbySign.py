class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            nums.sort(reverse=True)
            return nums
        
        positives, negatives = [], []
        for i in range(len(nums)):
            if nums[i] < 0:
                negatives.append(nums[i])
            else:
                positives.append(nums[i])
        ans = []
        for i in range(len(nums)//2):
            ans.append(positives[i])
            ans.append(negatives[i])
            
        
        return ans