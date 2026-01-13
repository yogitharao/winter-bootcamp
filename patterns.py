class Solution(object):
    def printPattern(self, n):
        for i in range(n):
            start = chr(ord('A') + n - i - 1)
            for j in range(i + 1):
                print(chr(ord(start) + j), end=" ")
            print()
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.printPattern(n)