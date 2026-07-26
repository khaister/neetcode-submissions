class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_point_index = len(nums) // 2
        
        if target < nums[mid_point_index]:
            return self._search(nums, 0, mid_point_index, target)
        return self._search(nums, mid_point_index, len(nums), target)

    def _search(self, nums: list[int], start_index: int, end_index: int, target: int) -> int:
        """
        start_index: where to start the search from inside the nums array (inclusive)
        end_index: where to stop the search from inside the nums array (exclusive)
        """
        print(f"{start_index=} {end_index=}")
        if end_index == start_index + 1:  # range has only 1 number
            return start_index if nums[start_index] == target else -1

        mid_point_index = ((end_index - start_index) // 2) + start_index
        
        if target < nums[mid_point_index]:
            return self._search(nums, start_index, mid_point_index, target)
        return self._search(nums, mid_point_index, end_index, target)
