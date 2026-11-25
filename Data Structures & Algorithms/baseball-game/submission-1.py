class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0 
        record = []
        for o in operations:
            if o == "+":
                x = record[-1]
                y = record[-2]
                record.append(x + y)
                score += (x+y)
            elif o == "C":
                score -= record[-1]
                record.pop()
            elif o == "D":
                x = record[-1]
                record.append(x * 2) 
                score += (x*2)
            else:
                record.append(int(o)) 
                score += int(o)
        return score       
        