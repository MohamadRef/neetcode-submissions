class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #we are using a set for effecient and it sorts the array into an order
        max_len = 0  #make max len 0

        for nums in num_set:  #iterate the nums in the set of nums
            if nums-1 not in num_set: #if the first number is not the start then make it the start
                current = nums 
                length = 1 #we count the first length of the start

                while current + 1 in num_set: #while its there in the nums we increment the current and the length
                    current +=1
                    length +=1
                max_len = max(max_len, length) #we return the max we found so far 

        return max_len #and call the function
