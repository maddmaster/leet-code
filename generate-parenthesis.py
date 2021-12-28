from typing import List


class Solution:
    def generate_parenthesis_iterative(self, n: int) -> List[str]:
        combinations = []
        if n == 0:
            return combinations
        else:
            possibilities = ["("]
            while possibilities:
                current = possibilities.pop()

                if len(current) == 2 * n:
                    combinations.append(current)
                    continue

                if current.count("(") < n:
                    possibilities.append(current + "(")

                if current.count(")") < current.count("("):
                    possibilities.append(current + ")")

            return combinations

    # applicable for smaller n, otherwise you will exceed the number of stacks...
    def generate_parenthesis_recursion(self, n) -> List[str]:
        def generate(combination, openings, closings, combinations=[]):
            print("params: {}, {}, {}".format(combination, openings, closings))
            if openings:
                generate(combination + '(', openings - 1, closings)

            if closings > openings:
                generate(combination + ')', openings, closings - 1)

            # we have used all the closings allocated to us...
            if not closings:
                combinations.append(combination)

            return combinations

        return generate('', n, n)


def main():
    solution = Solution()
    print(solution.generate_parenthesis_iterative(3))
    print(solution.generate_parenthesis_recursion(3))


if __name__ == '__main__':
    main()
