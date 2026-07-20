class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map < int, int > valueIndex;

        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
         if (valueIndex.find(complement) != valueIndex.end()) {
                return {valueIndex[complement], i}; // Return the indices
            }

            // Add the current number and its index to the map
            valueIndex[nums[i]] = i;
        }

        return {}; // Return an empty vector if no solution is found
    }
};