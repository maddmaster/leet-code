from typing import List


class Solver:
    def max_area_On2(self, heights: List[int]) -> int:
        max_area: int = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                # left side would be heights[i]
                # right side would be heights[j]
                # actual height would be min(heights[i], heights[j])
                height = min(heights[i], heights[j])
                width = j - i
                area = width * height

                if area > max_area:
                    print("{}, {}, {}, {}".format(i, j, heights[i], heights[j]))
                    max_area = area

        return max_area

    def max_area_On(self, heights: List[int]) -> int:

        max_area = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            # the area is a function of length and width
            # width would always be decreasing
            # this means that the only possibility that the area will increase is if the
            # height increases
            height = min(heights[i], heights[j])
            width = j - i
            area = width * height

            print("{}, {}, {}, {}, {}".format(i, j, heights[i], heights[j], area))
            if area > max_area:
                max_area = area

            # lets change side one at a time
            # if the left side is lower than the right side, lets increment i
            # if the right side is lower than the left side, lets decrement j
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == '__main__':
    solver = Solver()

    heights: List[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(solver.max_area_On2(heights))
    print(solver.max_area_On(heights))
