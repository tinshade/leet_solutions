class Solution:
    def sumOddLengthSubarrays(self, arr):
        
        n = len(arr)
        if n == 1:
            return arr[0]
        
        arr_sum, odds = sum(arr), 3
        if n == 3:
            return sum(arr)*2
        
        
        answer = 0 + arr_sum
        
        if n % 2 != 0:
            answer += arr_sum

        while odds < n:
            start, end = 0, odds
            
            while end <= n:
                answer += sum(arr[start:end])
                start += 1
                end += 1
            
            odds+=2
            
        return answer


if __name__ == "__main__":
    s=Solution()
    arr = [6,9,14,5,3,8,7,12,13,1]
    print(s.sumOddLengthSubarrays(arr)) # 878
    arr = [1,4,2,5,3]
    print(s.sumOddLengthSubarrays(arr)) # 58
    arr = [1]
    print(s.sumOddLengthSubarrays(arr)) # 1
    arr = [1,2]
    print(s.sumOddLengthSubarrays(arr)) # 3
    arr = [10,11,12]
    print(s.sumOddLengthSubarrays(arr)) # 66
