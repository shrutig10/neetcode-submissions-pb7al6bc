class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # might need to carry
        # travserse both string backwards
        # if both a and b are 1: carry--> 1, ouput = carry
        # if both are 0 --> make it carry, carry = 0
        # output = 1 + carry, carry 

        res = ''
        carry = 0

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0

            total = digitA + digitB + carry
            res = str((total % 2)) + res
            carry = total // 2

            i -= 1
            j -= 1

        return res