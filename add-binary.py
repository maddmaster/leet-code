class Solution:
    def add_binary(self, a: str, b: str) -> str:
        num1 = [int(x) for x in list(reversed(list(a)))]
        num2 = [int(x) for x in list(reversed(list(b)))]

        len1 = len(num1)
        len2 = len(num2)

        sum_of_nums = []
        carries = [0]

        for i in range(max(len1, len2)):
            digit1 = num1[i] if i < len1 else 0
            digit2 = num2[i] if i < len2 else 0

            sum_of_digits = digit1 + digit2 + carries[i]

            carry = sum_of_digits // 2

            sum_of_nums.append(sum_of_digits % 2)
            carries.append(carry)

            if i == max(len1, len2) - 1 and carry > 0:
                sum_of_nums.append(carry)

            print("{}, {}, {}, {}, {}".format(digit1, digit2, sum_of_digits, sum_of_nums, carries))

        return "".join([str(i) for i in list(reversed(sum_of_nums))])


if __name__ == "__main__":
    solution = Solution()

    a = "11"
    b = "11"

    solution.add_binary(a, b)