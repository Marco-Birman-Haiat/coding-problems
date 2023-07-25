class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeConstructor:
    def __init__(self, nodes_data) -> None:
        self.root = TreeNode()

    # def populate_tree(self, nodes_data):
    #     helper = self.root
    #     left = right = TreeNode()
    #     counter = 0
    #     for el in nodes_data:
    #         if counter % 2 == 0:
    #             helper = right
    #             right = TreeNode(el)
    #             helper.right = right
    #         if counter % 2 == 1:
    #             helper = left
    #             left = TreeNode(el)
    #             helper.left = left
