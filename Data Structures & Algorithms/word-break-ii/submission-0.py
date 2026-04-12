class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # check that the word can be broken up
        # while we are checking the word can be broken
        # if not out of bounds and = word, set dp[i] = dp[i + len(word)]
        # if dp[i] true, then we can have store the words that allow for it
        # another list of arrays storing which words makes it true
        # we can go through this list of arrays and create sentences
        # backtrack through the list of arrays <- have to start from index 0

        dp = [False] * (len(s) + 1)
        words = [[] for _ in range(len(s))]   
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    words[i].append(word)

        sentences = []

        def dfs(idx, curString):
            if idx >= len(words):
                sentences.append(" ".join(curString))
                return
            for segment in words[idx]:
                curString.append(segment)
                dfs(idx + len(segment), curString)
                curString.pop()
        
        dfs(0, [])
        return sentences

