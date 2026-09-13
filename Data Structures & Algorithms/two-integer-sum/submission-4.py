class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        num_to_index_map = {}

        for current_index, val in enumerate(nums):

            complement = target - val

            if complement in num_to_index_map:
                return [num_to_index_map[complement], current_index]

            else:

                num_to_index_map[val] = current_index
        