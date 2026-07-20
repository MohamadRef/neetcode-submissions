class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groupAnagrams; // Fix missing `>`

        for (const string& word : strs) { // Fix `const&` to `const string&`
            string sortedWord = word; // Fix variable name (`sortedwords` → `sortedWord`)
            sort(sortedWord.begin(), sortedWord.end()); // Sort the word
            groupAnagrams[sortedWord].push_back(word); // Group words by sorted key
        }

        vector<vector<string>> result; // Fix variable type
        for (const auto& group : groupAnagrams) {
            result.push_back(group.second); // Collect grouped anagrams
        }

        return result;
    }
};
