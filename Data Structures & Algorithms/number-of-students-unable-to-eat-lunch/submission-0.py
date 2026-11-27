class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        hungry = len(students)
        for s in sandwiches: 
            if count[s] == 0:
                break 
            else: 
                hungry -= 1
                temp = count[s] - 1
                count[s] = temp 
        return hungry 


    






        