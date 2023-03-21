class Solution:
    def isValid(self, s: str) -> bool:
        s_len = len(s)
        brackets = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        
        stack = []
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
