class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif len(needle) > len(haystack):
            return - 1
        elif haystack == needle:
            return 0
        else:
            size_of_needle = len(needle)
            for i in range(len(haystack) - size_of_needle + 1):
                substr = haystack[i:i + size_of_needle]
                if substr == needle:
                    return i

            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.str_str("abc", "c"))