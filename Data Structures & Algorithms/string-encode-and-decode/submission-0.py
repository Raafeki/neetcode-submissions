class Solution:

    def encode(self, strs: List[str]) -> str:

        res = "" # encoding the list of strs into a sing string

        for word in strs:
            res += str(len(word)) + "#" + word #len + delim + string
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):  #while pointer is still in bounds

            j = i # set j ptr to i
            while s[j] != "#":  # while j ptr is not at a delim
                j += 1 # move it along
            length = int(s[i:j]) # when it hits a delim, set length to i (begining) to where j at
            res.append(s[j + 1 : j + 1 + length]) # append first char of str to last (based on length)
            i = j + 1 + length # move to next string
        return res

