class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        maxi = 0
        for n in nums:
            if n == 1:
                counter+= 1
                maxi = max(maxi, counter)
            else:
                counter = 0 
            
        return maxi

        