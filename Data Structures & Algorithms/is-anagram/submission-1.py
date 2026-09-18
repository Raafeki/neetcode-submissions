class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # anagrams are strings that have the same characters the 
        # same amount of time

        # so we need to count the char


        if len(s) != len(t):   # check if length's r same
            return False

        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


