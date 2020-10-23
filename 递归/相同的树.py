# 100
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def isSameTree( p: TreeNode,q: TreeNode):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.data!=q.data:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

print(isSameTree())