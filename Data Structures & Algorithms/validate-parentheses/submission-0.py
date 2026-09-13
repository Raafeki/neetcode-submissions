class Solution:
    def isValid(self, s: str) -> bool:

        # a regular python list but we are utilizing it like a stack
        stack = []

        # hashmap with the closing braces as keys and opening as values
        closeToOpen = { ")" : "(",  "]" : "[", "}" : "{"}

        # for character in the string s
        for c in s:
            if c in closeToOpen:  # if the character is in the hashmap
                if stack and stack[-1] == closeToOpen[c]:  # check if the stack is empty AND if the value at the stop of the stack is the matching close par
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False