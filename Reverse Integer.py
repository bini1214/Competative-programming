class Solution:
    def reverse(self, x: int) -> int:

        reversed = 0 
        sign = 1

        if not  -2147483648 < x < 2147483647 :
            return 0

        if x < 0 :
            sign = -1 
            x *= sign 

        while (x > 0) :
            a = x % 10
            reversed = reversed * 10 + a
            x = x // 10
