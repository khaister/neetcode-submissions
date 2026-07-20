class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        sorted_nums = sorted(nums)
        for index, num in enumerate(sorted_nums):
            # since array is sorted, if first number is positive, remaining numbers would also be positive
            # so no possible way to have a sum of any 3 numbers equal to zero
            if num > 0:
                break

            # if the current number (from second item in the list)
            # is the same as the one before it, then finding the other
            # 2 numbers from the rest of the array would result in
            # duplicate results, so we need to skip
            if index > 0 and num == sorted_nums[index - 1]:
                continue

            # start a 2 pointer search to find nums[i] + nums[j] == 0 - num
            # similar to the 2 pointer problem for a sorted array
            i = index + 1
            j = len(sorted_nums) - 1
            while i < j:
                total = num + sorted_nums[i] + sorted_nums[j]

                # if total is bigger than 0 target, then move right pointer left
                # to get a smaller number
                if total > 0:
                    j -= 1

                # if total is less than 0 target, then move left pointer right
                # to get a larger number
                elif total < 0:
                    i += 1

                else:  # total == 0
                    results.append([num, sorted_nums[i], sorted_nums[j]])
                    i += 1
                    j -= 1
                    
                    # dedupe
                    while sorted_nums[i] == sorted_nums[i - 1] and i < j:
                        i += 1

        return results
