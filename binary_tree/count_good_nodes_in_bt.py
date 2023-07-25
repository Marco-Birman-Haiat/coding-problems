## It's not possible to execute the code locally since the binary tree is not yet implemented here.
## Such detail is manage by leetcode in their websit

def goodNodes(root) -> int:
  
  def findGood(root, max_val):
      if not root:
          return 0
      gn = 1 if root.val >= max_val else 0
      left_max = root.val if root.left == None else root.left.val
      right_max = root.val if root.right == None else root.right.val
      return (gn + findGood(root.left, max(max_val, left_max))
              + findGood(root.right, max(max_val, right_max)))
    
  return findGood(root, root.val)
        