class Solution:
    def convert(self, input: str, rows: int) -> int:
        lines = [''] * rows

        j = 0
        k = rows - 1
        for i in range(len(input)):
            if j < rows:
                lines[j] += input[i]
                j += 1

            if j >= rows:
                if 1 <= k <= rows - 2:
                    lines[k] += input[i]
                k -= 1

            if k == 0 and j >= rows:
                j = 0
                k = rows - 1

        return ''.join(lines)



if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))

