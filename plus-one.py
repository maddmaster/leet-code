from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        digits.insert(0, 0)

        for i in range(len(digits) -1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

            if digits[i] >= 10:
                digits[i-1] = digits[i-1] + digits[i] // 10
                digits[i] = digits[i] % 10

        if digits[0] == 0:
            digits.pop(0)

        return digits


if __name__ == "__main__":
    solution = Solution()

    input = [8]
    print(solution.plus_one(input))