class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # iterate the left hand with 0 first
            for j in range(i+1, len(nums)):  # and compare it with the right hand which is i+1, bcz the question says you cant use i = j
                if nums[i] + nums[j] == target:  # if the target is found, we return the indice of the nums that got us the target
                    return [i, j]
