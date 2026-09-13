class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # quick check to remove any strings that are not equal in length
        if len(s) != len(t):
            return False

        # create empty hashmap
        count_s, count_t = {}, {}

        # store strings into independent hashmaps 
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for c in count_s:
            if count_s[c] != count_t.get(c,0):
                return False
        

        # compare other string to hash set, if equal return true
        return count_s == count_t