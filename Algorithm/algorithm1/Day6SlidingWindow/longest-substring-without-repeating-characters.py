class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        mp = dict()
        start_position = 0
        for i in range(len(s)):
            if ord(s[i]) in mp.keys():
                start_position = max(start_position, mp[ord(s[i])] + 1)
            max_length = max(max_length, i - start_position + 1)
            mp[ord(s[i])] = i
            #print(i, start_position, max_length)
        return max_length



def test():
    for i in range(5, 10):
        print(i)

test()