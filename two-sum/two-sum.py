class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = dict(zip(nums, range(0, len(nums))))
        for i, num in enumerate(nums):
            if target-num in index_dict:
                if index_dict[target-num] != i:
                    return index_dict[target-num], i
        