class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for word in strs:
            if not res:
                res.append([word])
                continue
            added = False
            for item in res:
                if sorted(word) == sorted(item[0]):
                    item.append(word)
                    added = True
            if not added:
                res.append([word])

        return res
            

            



        