from typing import List

# use DFS
class Solution:
    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        current_partition = []

        def dfs(i):
            # check the base case first since this is a recursive function and we need to define our exit
            if i >= len(s):
                partitions.append(current_partition.copy())
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    current_partition.append(s[i:j+1])
                    dfs(j + 1)
                    current_partition.pop()

        dfs(0)
        return partitions


if __name__ == "__main__":
    pass


'''

'''