class Solution:
    def reverse(self, x: int) -> int:
        # need to know max positive value, and min negative value
        # extract each digit by doing x % 10
        # before adding to result, consider overflow
        # if not overflow, add digit to result by doing res * 10 + digit
        # how to check overflow
        # doing 2 operations when adding to result
        # multiplying then adding --> separate test cases
        # multiplying:
        # check that res > max / 10 or res < min / 10, multiplying by 10 will result in overflow
        # adding:
        # if res == max / 10 and the digit > max % 10, can't add
        # if res = min / 10 and the digit is < min % 10, can't add

        MIN = -2147483648
        MAX = 2147483647

        res = 0

        while x != 0:
            digit = int(math.fmod(x, 10))
            if res > (MAX // 10) or res < (MIN // 10):
                return 0
            if res == (MAX // 10) and digit > MAX % 10 or res == (MIN // 10) and digit < (MIN % 10):
                return 0
            res *= 10
            res += digit
            x = int(x / 10)

        return res
        
        
        