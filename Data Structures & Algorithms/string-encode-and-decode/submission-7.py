class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + '#'
            res += string
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur_ind = 0

        while cur_ind < len(s):
            cur_str = ""
            length = ""
            while(s[cur_ind] != '#'):
                length += s[cur_ind]
                cur_ind += 1

            cur_len = int(length)
            cur_ind += 1

            for i in range(cur_len):
                cur_str += s[cur_ind]
                cur_ind += 1
            res.append(cur_str)

        return res
