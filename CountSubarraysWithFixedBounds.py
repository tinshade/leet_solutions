
class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        out_of_bound_index = -1
        mi_index = -1
        ma_index = -1

        result = 0

        for index,number in enumerate(nums):
            # Checking if the number is out of bounds and updating index accordingly
            # Using <= since minK and maxK are also inclusive
            if not minK <= number <= maxK:
                out_of_bound_index = index
            
            # Not using ELIF as it might fail if both minK and maxK are the same number and maxK would never get updated, resulting in a 0.
            # Finding lower-bound number's index and updating mi_index
            if number == minK:
                mi_index = index
            
            # Finding upper-bound number's index and updating ma_index
            if number == maxK:
                ma_index = index

            # Identifying starting point for the loop
            # Lowest if the indices will mark our loop's start point.
            starting_point = min(mi_index, ma_index) 

            
            if starting_point > out_of_bound_index:
                result += (starting_point - out_of_bound_index)
            
        return result