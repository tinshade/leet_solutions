class Solutuion:
    def minimumSum(self, num:int) -> int:
        '''
            You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

            For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
            Return the minimum possible sum of new1 and new2.
        '''
        numbers = [
            num%10000//1000,
            num%1000//100,
            num%100//10,
            num%10
        ]
        numbers.sort() # This may be improved, IDK.
        num1 = numbers[0]*10 + numbers[2]
        num2 = numbers[1]*10 + numbers[3]
        return num1+num2




if __name__ == "__main__":
    s = Solutuion()
    print(s.minimumSum(2932)) # 52
    print(s.minimumSum(4009)) # 13