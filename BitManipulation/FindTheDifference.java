class Solution {
    public char findTheDifference(String s, String t) {
        
        // xor is associative, so it doesn't matter what order you perform it in.
        // when you xor a number with itself, the result is 0 
        // so if you xor every integer in the array with eachother, the result will be the unique number

        // TIME COMPLEXITY: O(n), where n is the total number of characters
        // SPACE COMPLEXITY: O(1)
        
        int xor = 0;
        
        for (char c : s.toCharArray()) {
            xor ^= c;
        }
        
        for (char c : t.toCharArray()) {
            xor ^= c;
        }
        
        return (char) xor;
    }
}
