class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def render_digits_sum(n):
            answer = 0
            for each in str(n):
                #* There are far better ways like taking modulo and getting digts that way.
                #* I was just lazy here.
                answer += int(each)
            
            return answer
        
        return abs(sum(nums) - sum(list(map(render_digits_sum, nums))))