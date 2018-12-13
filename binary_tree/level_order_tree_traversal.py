class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def print_level_order(root):
    h = _height(root)
    for i in range(1, h + 1):
        print_given_level(root, i)


def print_given_level(root, level):
    if root is None:
        return
    elif level == 1:
        print(root.val, end=' ')
    else:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)


# Compute the height of tree
def _height(node):

    if node is None:
        return 0
    else:
        left_height = _height(node.left)
        right_height = _height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

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
height = _height(root)
print(height)
print_level_order(root)