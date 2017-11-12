class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # neat solution with
        # O(n) time complexity
        # using a stack
        
        # will probably clean this up
        # and make the code more concise later
      
        stack = []
        for c in s:
            # push opening brackets onto the stack
            if c in "{([":
                stack.append(c)
            # if it's a closing bracket, pop the stack
            # and check the return value
            else:
                # if the stack is empty but you reach a closing
                # bracket, it's unbalanced
                if not stack:
                    return False
                if c == '}':
                    # make sure the balance property holds
                    if stack.pop() == '{':
                        continue
                    else:
                        return False
                if c == ']':
                    # make sure the balance property holds
                    if stack.pop() == '[':
                        continue
                    else:
                        return False
                if c == ')':
                    # make sure the balance property holds
                    if stack.pop() == '(':
                        continue
                    else:
                        return False
                    
        # if the stack still has brackets in it, then it's unbalanced
        return False if stack else True
