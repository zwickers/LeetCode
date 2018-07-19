class Solution {
    public String toHex(int num) {
        
        if (num == 0) return "0"; 
        
        int bitMask = 0b1111; 
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < 32; i += 4) {
            
                int hexDigit = (num >>> i) & bitMask;
            
                if (hexDigit < 10) {
                    sb.append(hexDigit);
                } 
                else {
                    
                    char c = (char) ('a' - 10 + hexDigit);
                    sb.append(c);
                    
                }

        }
            
        
        StringBuilder s = new StringBuilder(sb.reverse());
    
        // get rid of leading zeros
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '0') {i++;}
            else {
                break;
            }
        }
        
        return s.substring(i).toString();
        
        }
      
        
}
