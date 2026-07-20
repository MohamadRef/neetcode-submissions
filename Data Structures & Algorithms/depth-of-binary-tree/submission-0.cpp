/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if( root == nullptr){
            return 0; //base case if root = 0 .
        }
        int leftDepth = maxDepth(root->left);  //depth of left subtree
        int rightDepth = maxDepth(root->right); //depth of right subtree
        return 1 + max(leftDepth,rightDepth); // 1 + max function is useful
    }
};

