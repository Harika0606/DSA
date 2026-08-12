class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        tot=0
        n=x
        while n>0:
            digit=n%10
            tot+=digit
            n=n//10
        if x%tot==0:
            return tot
        return -1