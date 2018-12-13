class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val, end=' ')
            self.in_order(node.right)

    def pre_order(self, node):
        if node:
            print(node.val, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val, end=' ')

    def level_order(self, node):
        queue = list()
        if node:
            queue.append(node)

        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    #     1
    #    / \
    #   2   3
    #  /   / \
    # 4   2   4
    #    /
    #   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)

Sol = Solution()
Sol.in_order(root)
print('\n')
Sol.pre_order(root)
print('\n')
Sol.post_order(root)
print('\n')
Sol.level_order(root)
