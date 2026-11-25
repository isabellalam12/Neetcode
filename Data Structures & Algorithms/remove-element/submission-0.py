class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer to valid non-vals 
        k = 0 
        # pointer that goes through each nums element 
        for n in nums:
            if n != val: 
                nums[k] = n
                k += 1
        return k
 

        

