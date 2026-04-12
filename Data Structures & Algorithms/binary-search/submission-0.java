class Solution {
    public int search(int[] nums, int target) {
        //binary search
        //left pointer-starts at 0 <- point to index
        //right pointer-start at length - 1
        //update left if num is less than target
        //update right if num is greater than target
        //left would be greater than the right

        int left = 0;
        int right = nums.length - 1;

        while(left <= right)
        {
            int currIndex = (left + right) / 2;

            if(nums[currIndex] == target)
                return currIndex;
            else if(nums[currIndex] < target)
                left = currIndex + 1;
            else
                right = currIndex - 1;
        }

        return -1;
    }
}
