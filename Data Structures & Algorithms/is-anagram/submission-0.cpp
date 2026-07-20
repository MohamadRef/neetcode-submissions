class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false; // If the sizes are different, they can't be anagrams
        }
        
        sort(s.begin(), s.end()); // Sort both strings
        sort(t.begin(), t.end());
        
        return s == t; // Compare the sorted strings
    }
};

