from typing import List


#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            cnt=0
            for j in nums:
                if i ==j:
                    cnt+=1

        if cnt>=2:
            return True

        return False

call=Solution()
print(call.hasDuplicate([1,2,3,4,5,5]))
