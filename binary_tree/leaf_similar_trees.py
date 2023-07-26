## It's not possible to execute the code locally since the binary tree is not yet implemented here.
## Such detail is manage by leetcode in their websit

def leafSimilar(root1, root2) -> bool:
    return leaf_sequence(root1) == leaf_sequence(root2)
    
def leaf_sequence(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    
    return leaf_sequence(root.left) + leaf_sequence(root.right)