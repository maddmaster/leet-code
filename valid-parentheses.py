from typing import List


class Solver:
    def is_valid(self, s: str) -> bool:
        openings: List[str] = ["(", "{", "["]
        closings: List[str] = [")", "}", "]"]

        stack = []

        for c in s:
            if c in openings:
                stack.append(c)

            if c in closings:
                index = closings.index(c)
                latest = stack.pop()
                if latest != openings[index]:
                    return False


        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    solver = Solver()

    input = "()"
    print(solver.is_valid(input))