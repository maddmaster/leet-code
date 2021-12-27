from typing import List
import itertools

class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        mappings = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        answer: List[str] = []

        sources = []
        for i in range(len(digits)):
            digit = int(digits[i])
            sources.append(list(mappings[digit]))

        combinations = list(itertools.product(*sources))
        print(combinations)

        return answer


def main():
    solution = Solution()

    digits = "234"
    answer = solution.letter_combinations(digits)
    print(answer)


if __name__ == "__main__":
    main()
