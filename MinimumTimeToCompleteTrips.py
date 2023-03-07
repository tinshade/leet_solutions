class Solution:
    def minimumTime(self, time, totalTrips) -> int:
        if len(time) == 1 and totalTrips == 1:
            return time[0]
        
        lo = 0
        hi = 10 ** 15 #Because the upper limit is stated to be 10^7
        def helper(mid):
            trips = 0
            for each in time:
                trips += mid // each 
            return trips >= totalTrips

        # Using Binary Search Approach
        while lo < hi:
            mid = (lo + hi) // 2
            # If helper says mid point is good enough or exact to cover the total number of trips,
            # we move our right pointer from the initial infinity to whatever the current mid is.
            # There will be a point where mid == totalTrips. That will be the answer. 

            # If helper says that mid is less than totalTrips, we move the left pointer
            # to one element after our current mid and continue with the loop.
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo # Returing left since we need the minimum number of trips and max is the worst case anyway.


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTime([1,2,3], 5)) # 3