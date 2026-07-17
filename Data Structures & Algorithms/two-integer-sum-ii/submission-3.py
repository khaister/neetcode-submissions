class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            # if sum of first and last number is bigger than target
            # we need to move the right pointer to left which is smaller than
            # current right number; if we move left pointer, the new sum
            # would be even bigger than target
            if total > target:  # 8 + 11 = 17 < 19
                j -= 1

            # otherwise, if the sum is smaller than target, we need to
            # move the left pointer to the right, to get a bigger number
            # as to increase the chance of hitting target
            elif total < target:  # 6 + 11 = 17 < 19
                i += 1

            # total == target
            else:
                return [i + 1, j + 1]

        return []  # return empty array as required by method signature
