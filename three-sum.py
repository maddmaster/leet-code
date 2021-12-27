from typing import List


class Solver:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        result: List[List[int]] = []

        # 1st + 2nd + 3rd = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # nums[i] is the 1st number
            # the sum of the 2nd and 3rd number would be equal to 0 - 1st
            required = 0 - nums[i]

            j = i + 1
            k = len(nums) - 1
            while j < k:
                actual = nums[k] + nums[j]

                # print("{}, {}, {}, {}, {}".format(i, j, k, actual, required))

                if actual < required:
                    j += 1
                elif actual > required:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result


if __name__ == "__main__":
    solver = Solver()

    nums = [-1, 0, 1, 2, -1, -4]

    solver.three_sum(nums)
