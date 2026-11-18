# input: 
    #string s: string to remove letters from 
    #integer k: number of adjacent & duplicate letters to remove at a time 
# output: string s after k removals 
# edge cases: s is empty --> "", s has no duplicates, k is 0 --> s 
# possible algorithm 
    # iterative go through the string removing groups of k adj/dup letters from s until you are able to iterate thru without changing the string 
    #
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s: 
            if stack and stack[-1][0] == char: 
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else: 
                stack.append([char, 1])
        # rebuild the string 
        string_result = ""
        for [char,count] in stack: 
            string_result+= (char*count)
        return string_result


        
        