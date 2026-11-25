class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', ']':'[', '}':'{' }
        stack = []
        for b in s: 
            if b in closeToOpen.values(): 
                stack.append(b)
            else: 
                if stack and stack[-1] == closeToOpen[b]:
                    stack.pop()
                else: 
                    return False
        return len(stack) == 0


        