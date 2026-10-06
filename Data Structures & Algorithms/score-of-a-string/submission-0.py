class Solution:
    def scoreOfString(self, s: str) -> int:
        

        # "c o d e"
        # 'c' = 99
        # 'o' = 111
        # 'd' = 100
        # 'e' = 101

        # |111 - 99| + |100 - 111| + |101 - 100|
        #   o  -  c  +   d  -  o       e  -  d  



        score = 0

        for char in range(len(s)-1):
            score += abs(ord(s[char+1]) - ord(s[char]))
        return score
        
