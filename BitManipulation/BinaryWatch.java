class Solution {
    
    // time complexity: O(1)
    // space complexity: O(1)
    
    public List<String> readBinaryWatch(int num) {
        
        ArrayList<String> res = new ArrayList<>();
        
        for (int hour = 0; hour < 12; hour++) {
            for (int minute = 0; minute < 60; minute++) {
                if (bitCount(hour) + bitCount(minute) == num) {
                    res.add(String.format("%d:%02d", hour, minute));
                }
            }
        }        
        
        return res;
        
    }
    
    private int bitCount(int num) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if (((num >> i) & 1) == 1) count++;
        }
        return count;
    }
    
}
