import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        self.total_hours_greater_than_h = None

        k_min = 1
        k_max = max(piles)

        k = math.ceil((k_max - k_min) / 2)
        
        total_hours = self._calc_total_hours(piles, k)
        print(f"{k=} {total_hours=}")
        if total_hours >= h:
            self.total_hours_greater_than_h = True
            return self._find_k(k, k_max)

        self.total_hours_greater_than_h = False
        return self._find_k(k_min, k)

    def _find_k(self, k_min, k_max) -> int:
        k = math.ceil((k_max - k_min) / 2) + k_min
        
        total_hours = self._calc_total_hours(self.piles, k)
        print(f"{k_min=} {k_max=} {k=} {self.total_hours_greater_than_h} {total_hours=}")
        # detect inflection point
        if (self.total_hours_greater_than_h and total_hours < self.h) or (not self.total_hours_greater_than_h and total_hours >= self.h):
            return k

        if total_hours > self.h:
            return self._find_k(k, k_max)
        return self._find_k(k_min, k)

    def _calc_total_hours(self, piles, k) -> int:
        """
        Calculates total number of hours koko would take
        to finish the pile if she eats k banana per hour
        """
        return sum(math.ceil(bananas / k) for bananas in piles)


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
