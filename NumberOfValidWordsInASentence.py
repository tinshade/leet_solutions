class Solution:
    def countValidWords(self, sentence: str) -> int:
        # sentence = "cat and  dog"
        sentence = sentence.split(' ')
        result = 0

        for i in range(len(sentence)):
            if sentence[i].isalpha():
                result += 1

        return result


s = Solution()
sentence = "cat and  dog"
print(s.countValidWords(sentence)) #3


sentence = "!this  1-s b8d!"
print(s.countValidWords(sentence)) #0

sentence = "alice and  bob are playing stone-game10"
print(s.countValidWords(sentence)) #5