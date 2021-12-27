class Solution:
    def length_of_last_word(self, s: str) -> int:
        i = len(s) - 1
        last_word = ""

        while s[i] == " " and i > 0:
            i -= 1

        while s[i] != " " and i >= 0:
            last_word += s[i]
            i -= 1

        return len(last_word)

if __name__ == "__main__":
    solution = Solution()

    input = "a "
    print(solution.length_of_last_word(input))
