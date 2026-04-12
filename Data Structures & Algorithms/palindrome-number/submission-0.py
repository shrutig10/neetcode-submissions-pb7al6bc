class Solution:
    def isPalindrome(self, x: int) -> bool:
        # grab each digit from original number and add to new number
        # return x == new number
        # how to build new number
        # multiply new number by 10 and then add the digit we got to that

        copy = x
        new_num = 0

        while copy > 0:
            digit = copy % 10
            new_num = new_num * 10 + digit
            copy = copy // 10

        return x == new_num

        
        