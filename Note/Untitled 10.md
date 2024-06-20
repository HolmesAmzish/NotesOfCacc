```cpp
/*
 * Program: binary-search-tree.cpp
 * Date: 2024.06.15
 * Author: Nulla
 * Description: Build a binary search tree by a sequence of numbers
 *              Print the tree by using parentheses
 */

#include <iostream>
#include <vector>
using namespace std;

struct BinaryTreeNode {
    int value;
    BinaryTreeNode *left_child;
    BinaryTreeNode *right_child;

    // Constructor
    BinaryTreeNode(int v) {
        value = v;
        left_child = nullptr;
        right_child = nullptr;
    }
};

void printTree(BinaryTreeNode* root) {
    if (root != nullptr) {
        cout << root->value;
        if (root->left_child != nullptr || root->right_child != nullptr) {
            cout << '(';
            printTree(root->left_child);
            cout << ',';
            printTree(root->right_child);
            cout << ')';
        }
    }
}

BinaryTreeNode* insertNode(BinaryTreeNode* root, int value) {
    // Set the new node if root is null
    if (root == nullptr) {
        return new BinaryTreeNode(value);
    }

    if (value < root->value) {
        root->left_child = insertNode(root->left_child, value);
    } else if (value > root->value) {
        root->right_child = insertNode(root->right_child, value);
    }

    return root;
}

void find(BinaryTreeNode* root, int key) {
    while (root != nullptr) {
        cout << root->value << ' ';
        if (key == root->value) break;
        
        if (key < root->value) {
            root = root->left_child;
        } else {
            root = root->right_child;
        }
    }
}

int main() {
    vector<int> sequence;
    int input, key;
    
    BinaryTreeNode* root = nullptr;
    while (cin >> input && input != -1) {
        root = insertNode(root, input);
        printTree(root);
        cout << endl;
    }

    cin >> key;
    find(root, key);
    
    return 0;
}
```

