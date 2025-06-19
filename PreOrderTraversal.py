#!/usr/bin/python3

from typing import Optional, List

# TreeNode definition (usually provided by LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.traverse(root)
        return self.values

    def traverse(self, node):
        if node is None:
            return
        self.values.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)

# Test case
def test_preorder_traversal():
    # Create a simple binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    result = solution.preorderTraversal(root)

    print(f"Tree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\")
    print("   4   5")
    print()
    print(f"Preorder traversal result: {result}")
    print(f"Expected: [1, 2, 4, 5, 3]")
    print(f"Test passed: {result == [1, 2, 4, 5, 3]}")

# Additional test cases
def test_edge_cases():
    solution = Solution()

    # Test empty tree
    result1 = solution.preorderTraversal(None)
    print(f"\nEmpty tree: {result1} (Expected: [])")

    # Test single node
    single_node = TreeNode(42)
    result2 = solution.preorderTraversal(single_node)
    print(f"Single node: {result2} (Expected: [42])")

    # Test left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    result3 = solution.preorderTraversal(left_skewed)
    print(f"Left-skewed tree: {result3} (Expected: [1, 2, 3])")

if __name__ == "__main__":
    test_preorder_traversal()
    test_edge_cases()
