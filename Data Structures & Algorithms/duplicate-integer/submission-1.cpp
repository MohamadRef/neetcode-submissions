class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Iterate through all pairs of elements in the array
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                // Compare elements at index i and j
                if (nums[i] == nums[j]) {
                    return true; // Return true if a duplicate is found
                }
            }
        }
        return false; // No duplicates found
    }
};

