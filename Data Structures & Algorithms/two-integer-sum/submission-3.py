class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_values = {}

        

        for index, value in enumerate(nums):
            
            number_we_need = target - value

            if number_we_need in seen_values:
                
                return [seen_values[number_we_need], index]

            else:

                seen_values[value] = index


\

                