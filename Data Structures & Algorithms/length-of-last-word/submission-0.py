class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
    
        i = len(s) - 1 # start iterator at end of string
        length = 0 

        while s[i] == ' ': #decrement while we have ending spaces
            i -= 1
        while i >= 0 and s[i] != ' ': # while incrementor is not 0 and we dont hit any spaces
            i -= 1 # we decrement and add to length, then return length
            length += 1
        return length


    