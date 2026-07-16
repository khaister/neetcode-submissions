class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            # if sum of first and last number is bigger than target
            # we need to move the right pointer to left which is smaller than
            # current right number; if we move left pointer, the new sum
            # would be even bigger than target
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue

            # otherwise, if the sum is smaller than target, we need to
            # move the left pointer to the right, to get a bigger number
            # as to increase the chance of hitting target
            else:
                i += 1
                continue

            if numbers[i] + numbers[j] == target:
                result = [i + 1, j + 1]

            i += 1
            j -= 1

        return result