class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; // Set to track unique elements
        for (int i = 0 ; i < nums.size() ; i++) {
            if (seen.count(nums[i])) { // Check if nums[i] is already in the set
                return true; // Duplicate found
            }
            seen.insert(nums[i]); // Add nums[i] to the set
        }
        return false; // No duplicates found
    }
};
