class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
            print(f"{lo=} {hi=}")
        return nums[lo]


"""
if i know how many n times the array was rorated, then the min is n + 1

if nums[0] < nums[-1], then it is either (a) the array was not rotated, or (b) n = len(nums)
   then min is nums[0]
else
   can we find mid point
   3 4 5 6 1 2
   ^         ^
  
"""
