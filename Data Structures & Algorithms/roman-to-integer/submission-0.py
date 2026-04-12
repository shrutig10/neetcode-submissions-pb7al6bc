class Solution:
    def romanToInt(self, s: str) -> int:
        # store the values of the roman numerals to their numerical value in a hashmap
        # iterate through the string and continuously add to a result
        # check that this numeral is not larger than the next
        # if it is larger than the numeral in front of it, then subtract that amount from result

        res = 0
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):
            if i < len(s) - 1:
                if numerals[s[i + 1]] > numerals[s[i]]:
                    res -= numerals[s[i]]
                    continue
            res += numerals[s[i]]

        return res        