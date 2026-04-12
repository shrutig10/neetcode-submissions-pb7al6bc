class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buying = prices[0];

        for(int i = 1; i < prices.length; i++)
        {
            if(prices[i] < buying)
                buying = prices[i];
            else
            {
                if(prices[i] - buying > profit)
                    profit = prices[i] - buying;
            }
        }

        return profit;
    }
}
