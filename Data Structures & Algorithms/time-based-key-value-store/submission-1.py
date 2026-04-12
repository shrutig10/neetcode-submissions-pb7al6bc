class TimeMap:

    def __init__(self):
        # use a map (key, [(timestamp, value)])

        self.mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # we will create this tuple and add it to the map
        self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # we can look for the timestamp if it exists, return the older most recent 
        # use a binary search
        # have a left and right that point to the ends of the array of the key
        # comparing the timestamp (array[mid][0]) with the timestamp given
        # if our left is out of bounds, return ""
        # otherwise if you can't find it, return l is at [(1, happy)]
        # if l == r, return whatever we have [(2, sad)] --> ""

        arr = self.mapping[key]
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                if arr[mid + 1][0] > timestamp:
                    return arr[mid][1]
                else:
                    l = mid + 1
            else:
                r = mid - 1
        
        if l == r and arr[l][0] <= timestamp:
            return arr[l][1]
        else:
            return ""
        
