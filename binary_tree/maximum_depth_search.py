## It's not possible to execute the code locally since the binary tree is not yet implemented here.
## Such detail is manage by leetcode in their websit

def maxDepth(self, root) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))