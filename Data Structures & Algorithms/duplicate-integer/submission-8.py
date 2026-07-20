class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = list() #created an empty list. why? to store the appended  nums 

        for num in nums: #a loop to itearte over the nums
            if num in seen:  # if has duplicates, it returns true
                return True
            seen.append(num)  # if no duplicate found it adds the iteartion to the empty list we created which is seen
        return False # no dups where found