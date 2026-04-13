class TimeMap:

    def __init__(self):
        # dictionary to hold key value 
        # value would contain timestamp and value
        # value will be a list of tuples
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add to the dictionary (create a new tuple and add)
        if key not in self.times:
            self.times[key] = [(timestamp, value)]
        else:
            self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # iterate through values of that key until we find exact match; else get most recent
        possible_vals = self.times.get(key, "")

        if not possible_vals:
            return possible_vals
        
        value = ""

        for time, val in possible_vals:
            if time <= timestamp:
                value = val
            else:
                break

        return value
            
