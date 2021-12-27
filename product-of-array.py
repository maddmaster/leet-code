from typing import List


def solve_On2(nums: List[int]) -> List[int]:
    solution: List[int] = []

    for i in range(len(nums)):
        product: int = None
        for j in range(len(nums)):
            if i != j:
                if product is not None:
                    product = product * nums[j]
                else:
                    product = nums[j]

        solution.append(product)

    return solution


def solve_3On(nums: List[int]) -> List[int]:
    solution: List[int] = [None] * len(nums)

    lefts: List[int]= [None] * len(nums)
    rights: List[int] = [None] * len(nums)

    lefts[0] = 1
    rights[len(nums) - 1] = 1

    # for each index / position we get the product of all numbers to it's left
    # and all the numbers to it's right and then multiply them together

    for i in range(1, len(nums)):
        lefts[i] = nums[i - 1] * lefts[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        rights[i] = nums[i + 1] * rights[i + 1]

    for i in range(len(nums)):
        solution[i] = lefts[i] * rights[i]

    return solution


if __name__ == "__main__":
    input = [1, 2, 3, 4]

    print(solve_On2(input))
    print(solve_3On(input))
