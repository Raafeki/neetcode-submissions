class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0
        r = len(nums) - 1 # the minus one accounts for 0-indexing


        while l <= r: # while left pointer doesn't cross right (check for middle elem if equal)
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
