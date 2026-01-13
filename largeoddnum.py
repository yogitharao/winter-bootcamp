class Solution:  
    def largeOddNum(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 1:  
                candidate = s[:i+1]  
                candidate = candidate.lstrip("0")
                return candidate
        return "" 
s=input()
sol=Solution()
print(sol.largeOddNum(s))