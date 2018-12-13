class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def search(self, node, key):
        if node is None or node.val == key:
            if node:
                print("find: ", key)
            else:
                print("Not found")
            return node

        if node.val < key:
            return self.search(node.right, key)

        return self.search(node.left, key)

    def insert(self, node, key):
        if node:
            if node.val < key:
                if node.right:
                    self.insert(node.right, key)
                else:
                    node.right = TreeNode(key)
            else:
                if node.left:
                    self.insert(node.left, key)
                else:
                    node.left = TreeNode(key)
        else:
            node = TreeNode(key)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val, end=' ')
            self.in_order(node.right)

    #     8
    #    / \
    #   3   12
    #  /   / \
    # 1   10   14
    #    /
    #   9

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(12)
root.left.left = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)
root.right.left.left = TreeNode(9)

Sol = Solution()
Sol.search(root, 2)
Sol.in_order(root)
Sol.insert(root, 11)
print('\n')
Sol.in_order(root)