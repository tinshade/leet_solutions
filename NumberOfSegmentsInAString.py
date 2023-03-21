class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip().split(' ')
        counter = 0
        for each in s:
            if each.strip() != '':
                counter += 1
        
        return counter



if __name__ == "__main__":
    s = Solution()
    print(s.countSegments('Hello')) # 1
    print(s.countSegments('Hello, my name is John')) # 5
    print(s.countSegments('')) # 0
    print(s.countSegments('", , , ,        a, eaefa"')) # 6