class Solution:

    def compress_new(self, chars):
        n = len(chars)
        if n == 1:
            return n
        
        # In-place array manipulation
        # Delete every elemement of the same nature after the first found element while keeping a count of the deletions
        # Once the element changes, add the counter as string and reset the counter.

        here = 0 # start replacing from here
        i = 0 # iterator
        while i < len(chars): #iterate through array
            char = chars[i] # current character 
            length = 1 # current characters length
            while i+1 < len(chars) and char == chars[i+1]: # the last char
                length += 1 # increase current chars length
                i += 1  # increment pointer/iterator
            chars[here] = char # replace the character at poisition with current char
            if length > 1: # only replace if current char is seen more than once
                len_str = str(length)
                chars[here+1:here + 1 + len(str(length))] = str(length) # here to there = length = repeat length of current char
                here += len(str(length)) # if length > 10, replace it as "1", "0" so "there" value changes
            here += 1 # if no repetitions, move on to the next char
            i += 1 # incrementing the iterator
        #print(chars[:here])
        return here
            


    def compress(self, chars) -> int:
        n = len(chars)
        if n == 1:
            return 1
        hashmap = {}
        for i in range(n):
            if chars[i] in hashmap:
                hashmap[chars[i]] += 1
            else:
                hashmap[chars[i]] = 1
        chars = []
        ret_len = 0
        for key, value in hashmap.items():
            chars.append(str(key))
            if value > 1:
                chars.append(str(value))
            ret_len += 1*2
        print(chars)
        return ret_len


if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a","a","b","b","c","c","c"])) #["a","2","b","2","c","3"], 6
    
