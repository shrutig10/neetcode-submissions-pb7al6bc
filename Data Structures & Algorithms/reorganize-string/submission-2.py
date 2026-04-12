
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # the highest frequency letter must be less than or equal to the total number of 
        # characters divided by 2

        # iterate through the string and get the frequency of each character --> put into max heap
        # do a quick check for the above condition --> return "" if not possible 
        # can put into heap as we go, when building a new string, hold the previous 
        # pop the top, add that character to return string
        # add the new character on
        # add the previous back into the heap
        # add the previous character into the return string

        if s == "":
            return s

        frequency = {}
        maximum = 0
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
            maximum = max(frequency[char], maximum)

        if maximum > ((len(s) // 2) + 1):
            return ""
        

        heap = []

        for letter, freq in frequency.items():
            heapq.heappush(heap, (-freq, letter))
        
        prev = None
        res = ""

        while heap:
            freq, letter = heapq.heappop(heap)
            res += letter
            freq += 1
            
            if prev:
                heapq.heappush(heap, prev)
            
            if freq < 0:
                prev = (freq, letter)
            else:
                prev = None
            
        if prev:
            return ""

        return res

                

