class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>1:
            n=n/3
        return n==1