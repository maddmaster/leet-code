from typing import List


class Solver:
    def three_sum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) == 3:
            return sum(nums)
        else:
            diff_x_int = {}

            nums.sort()

            # get the diffs
            for i in range(len(nums)):
                diff = target - nums[i]
                diff_x_int[diff] = nums[i]

            print(diff_x_int)

            diffs = list(diff_x_int.keys())
            diffs.sort()
            print(diffs)

            # diffs closest to zero should be what we want
            smallest = min([(abs(x), x) for x in diffs])[1]
            smallest_index = diffs.index(smallest)
            print("{}, {}".format(smallest, diffs.index(smallest)))

            from_index = max(0, smallest - 2)
            to_index = min(smallest + 2, len(diffs))

            smallest_sum = None

            for i in range(from_index, smallest_index + 1):
                sum = diff_x_int[diffs[i]] + diff_x_int[diffs[i + 1]] + diff_x_int[diffs[i + 2]]
                print("{}, {} + {} + {} = {}".format(i, diffs[i], diffs[i + 1], diffs[i + 2], sum))
                if smallest_sum is None:
                    smallest_sum = sum
                elif sum < smallest_sum:
                    smallest_sum = sum
                else:
                    pass

            return smallest_sum

    def three_sum_On2(self, nums: List[int], target: int) -> int:
        smallest_diff = None
        smallest_sum = None

        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                print("{}, {}, {}".format(i, j, k))

                sum = nums[i] + nums[j] + nums[k]

                diff = abs(sum - target)

                if diff == 0:
                    return sum

                if smallest_diff is None:
                    smallest_diff = diff
                    smallest_sum = sum

                if sum <= target:
                    j += 1
                else:
                    k -= 1

        return smallest_sum

    def three_sum_On(self, nums: List[int], target: int) -> int:
        """
        we have a sorted array of numbers
        i is static, j moves to higher values, k moves to lower values

        """

        nums.sort()

        smallest_diff: int = None
        closest_sum: int = None

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)

                if smallest_diff is None or diff < smallest_diff:
                    smallest_diff = diff
                    closest_sum = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    return sum

        return closest_sum


def main():
    solver = Solver()

    nums = [-1, 2, 1, -4]

    sum = solver.three_sum_On(nums, 1)
    print(sum)


if __name__ == "__main__":
    main()