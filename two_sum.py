from typing import List, Dict


"""
Runtime: 57ms, Beats 73.57%
Memory: 17.68MB, Beats 49.90%
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int, int] = {}
        for index, value in enumerate(nums):
            another_index = num_dict.get(target - value, None)
            if another_index is not None:
                return [index, another_index]
            num_dict[value] = index
