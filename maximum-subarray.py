from typing import List


class Solution:
    def use_kadane(self, nums: List[int]) -> int:
        largest: int = None
        curr: int = 0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num

            if largest is None:
                largest = curr
            else:
                largest = max(largest, curr)

        return largest

    def use_kadane_2(self, nums:List[int]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.use_kadane(nums))

