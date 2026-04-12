class Solution {
    public boolean isAnagram(String s, String t) {
        //create a hashmap that maps letters to their frequencies in s
        //loop through s and add letters to the hashmap or increment the frequency
        //loop through t
        //for each letter, if it is in hashmap, decrement the frequency of that letter
        //if the letter in the hashmap maps to 0, remove it from the hashmap
        //if the letter is not in the hashmap, automatically return false

        //after looping through t
        //return size of the hashmap is 0
        //if it is 0, t is an anagram of s, otherwise it is not

        //automatically know that s and t are not anagrams if they are different lengths

        if(s.length() != t.length())
            return false;

        HashMap<Character, Integer> frequency = new HashMap<>();
        for(int i = 0; i < s.length(); i++)
        {
            char curr = s.charAt(i);
            if(frequency.containsKey(curr))
            {
                frequency.put(curr, frequency.get(curr) + 1);
            }
            else
            {
                frequency.put(curr, 1);
            }
        }

        for(int i = 0; i < t.length(); i++)
        {
            char curr = t.charAt(i);
            if(frequency.containsKey(curr))
            {
                frequency.put(curr, frequency.get(curr) - 1);
                if(frequency.get(curr) == 0)
                    frequency.remove(curr);
            }
            else
            {
                return false;
            }
        }

        return frequency.size() == 0;

    }
}
