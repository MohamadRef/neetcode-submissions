class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> target_indices;
        int n = nums.size();
        for( int i = 0; i < n ; i++){
            for( int j = i + 1 ; j < n ; j++){
                if( nums.at(i) + nums.at(j) == target){
                    target_indices.push_back(i);
                    target_indices.push_back(j);
                    return target_indices;
                }
            }
        }
        return target_indices;
    }
};
