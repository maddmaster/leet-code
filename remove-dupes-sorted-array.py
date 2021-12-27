from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:

        j = 0

        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                j += 1
                nums[j] = nums[i]

        return j + 1

if __name__ == '__main__':
    pass