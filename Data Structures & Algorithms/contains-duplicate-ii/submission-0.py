class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # need to keep track of numbers we have seen before <- hash map
        # iterate through nums
        # if we have not seen the number before
        # add it to the hashmap (num --> idx)
        # if we have seen the number before
        # subtract hashmap[num] and current idx 
        # if this is less than k, then return true, else keep going and replace idx with new idx

        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping:
                if abs(mapping[nums[i]] - i) <= k:
                    return True
            mapping[nums[i]] = i

        return False    
        