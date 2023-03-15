class Solution:
    def sortSentence(self, s:str)->str:
        answer = ['','','','','','','','','','']
        for each in s.split(' '):
            answer[int(each[-1])] = each[:-1]
        return ' '.join(answer).strip()



if __name__ == "__main__":
    s = Solution()
    print(s.sortSentence("is2 sentence4 This1 a3")) # This is a sentence
    print(s.sortSentence("Myself2 Me1 I4 and3")) # Me Myself and I
    print(s.sortSentence("QcGZ4 TFJStgu3 HvsRImLBfHd8 PaGqsPNo9 mZwxlrYzanuVOUZoyNjt1 fzhdtYIen6 mV7 LKuaOtefsixxo5 pwdEK2")) # mZwxlrYzanuVOUZoyNjt pwdEK TFJStgu QcGZ LKuaOtefsixxo fzhdtYIen mV HvsRImLBfHd PaGqsPNo
