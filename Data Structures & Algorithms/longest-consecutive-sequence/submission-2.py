class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # check if there is a left neighbor
        # if so, then start the sequence
        # check if the next val in sequence is in the set

        check = set(nums)
        longest = 0


        for n in nums:
            if n-1 not in check:  # if the number before the current num is not in the set
                length = 1 # start the length at 1, since this is the beginning 
                while (n + length) in check:  # while the curr num + the length is in check
                    length += 1  # we add to the length
                longest = max(length, longest)  # then we keep the longest length thus far
        return longest  # and we're done
            