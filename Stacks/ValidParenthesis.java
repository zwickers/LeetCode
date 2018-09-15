class Solution {
    public boolean isValid(String s) {
        
        if (s.length() == 0) {
            return true;
        }
        
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            
            char c = s.charAt(i);
            
            if (c == '(' || c == '{' || c == '[') {
                stack.push(s.charAt(i));
            } 
            else {
                if (!stack.isEmpty()) {
                    if (c == ')' && stack.pop() != '(') {
                        return false;
                    }
                    else if (c == '}' && stack.pop() != '{') {
                        return false;
                    }
                    else if (c == ']' && stack.pop() != '[') {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }
        
        return (stack.isEmpty()) ? true : false;
    }
}
