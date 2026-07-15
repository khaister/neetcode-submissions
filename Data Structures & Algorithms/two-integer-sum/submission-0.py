class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for index, num in enumerate(nums):
            other_num = target - num
            if seen.get(other_num) is not None:
                result.extend([seen[other_num], index])
            else:
                seen[num] = index
        return result
