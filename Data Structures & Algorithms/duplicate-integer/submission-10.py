class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # given array nums 
        # check in the array has any similar values
        # return true if yes and false if no

        seen = set()
        for num in nums:
            if num in seen:
                return True 
            else:
                seen.add(num)
        return False
        


            
        