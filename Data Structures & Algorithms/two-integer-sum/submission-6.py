class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} #ig we are using a dictionary over here
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]

            m[nums[i]] = i
