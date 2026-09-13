class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        # set is more appropiate when you need to check presense
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i) 

        return False