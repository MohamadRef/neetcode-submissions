class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}  # the hash map

        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1 # add 1 
            else:
                m[nums[i]] += 1 #increment if alr seen 

        numbers = sorted(m.keys(), key = lambda x: m[x], reverse=True)
        #we use reverse  = True to get the largest, if not done that= i will be smallest
        return numbers[:k]

        # if dont wanna use the lambda, create a def and write def get_freq(x):
        #                                                           return m[x]