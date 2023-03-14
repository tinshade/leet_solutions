class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = format(n, '032b')
        reversed_str = binary_str[::-1]
        reversed_int = int(reversed_str, 2)
        
        return reversed_int





if __name__ == "__main__":
    '''
        Input: n = 00000010100101000001111010011100
        Output:    964176192 (00111001011110000010100101000000)
        Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
    '''
    s = Solution()
    print(s.reverseBits(int(00000010100101000001111010011100)))