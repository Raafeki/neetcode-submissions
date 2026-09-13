class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        no_spaces = "".join(ch.lower() for ch in s if ch.isalnum())


        reversed_s = ""

        for i in range(len(no_spaces)-1,-1,-1):
            reversed_s += no_spaces[i]

        if reversed_s == no_spaces:
            return True

        return False