class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        # l can not surpass r, otherwise it is out of bounds of the array
        while l <= r:
            
            
            m = (l+r) // 2

            if nums[m] > target:
                r = m - 1
             
            elif nums[m] < target:
                l = m + 1

            else:
                return m
        
        return -1
