class Solution:
    def maxDepth(self, s: str) -> int:

        # input: string with parentheses
        # output: max number of parenthesis 
        # edge: no parenthesis --> 0; no opening parenthesis 
        # approach: stack 
            # push: when open parenthesis 
                # check and update max by checking the size of stack 
            # pop: when closed parenthsis 
        stack = []
        maxParentheses = 0
        for c in s: 
            if c == "(": 
                stack.append(c)
                maxParentheses = max(maxParentheses, len(stack))
            elif c == ")": 
                stack.pop()
        return maxParentheses


        
        
        