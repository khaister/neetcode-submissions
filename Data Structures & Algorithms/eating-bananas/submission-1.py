import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum([math.ceil(bananas / k) for bananas in piles])

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (hi - lo) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo


"""
piles = [1,4,3,2], h = 9

k = 1, hours = 10 > 9 !
k = 2, hours = 6
k = 3, hours = 5
k = 4, hours = 4
k = 5, hours = 4
k = 6, hours = 4
---

piles = [25,10,23,4], h = 4

k = 1, hours = 25 + 10 + 23 + 4 = 62
k = 12, hours = 3 + 1 + 2 + 1 = 7
---

k_min = 1
k_max = max(piles)

if h equals len(piles), k is at least k_max
"""
