class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}  
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
            else:
                m[nums[i]] += 1
        numbers = sorted(m.keys(), key = lambda x: m[x], reverse=True)
        return numbers[:k]