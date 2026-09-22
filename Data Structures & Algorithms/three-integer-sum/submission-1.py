class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         

        nums.sort()
        res = []
        
         


        for i in range(len(nums)):
            l = i + 1 # start after i
            r = len(nums)-1
            while l < r:
                comb = nums[i] + nums[l] + nums[r]
                if comb == 0 and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif comb < 0:
                    l+= 1
                else:
                    r-= 1
        return res