
import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 2. if the max freq is more than half the string, return ""
        # 1. get frequencies for each character --> dictionary (char, freq), store the max freq seen
        # 3. build new string: prioritize higher frequently appearing characters
        #   do this using a max-heap (ordered by frequency)
        #   iterate as long as there are items in the heap and then add the char at the top of heap
        #   if > 1 freq, store in prev, add back with one less freq on next iteration
        # 4. once our heap is empty, then return string
        #    extra check: if prev has a value, then return ""; same character appears twice


        freq = defaultdict(int)
        maxFreq = 0
        for char in s:
            freq[char] += 1
            maxFreq = max(maxFreq, freq[char])

        if maxFreq > (len(s) + 1) // 2 :
            return ""

        maxHeap = [(-freq, char) for char, freq in freq.items()]

        heapq.heapify(maxHeap)

        res = ""
        prev = None

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res += char

            if prev:
                heapq.heappush(maxHeap, prev)
            
            freq += 1
            if freq < 0:
                prev = (freq, char)
            else:
                prev = None
        
        return res


        


        