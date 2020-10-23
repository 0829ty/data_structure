class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.Parent=None
    def __repr__(self):
        pass

class Tree:
    def __init__(self):
        self.root=None
    def diaohuan(self,node,childern):
        # 找父亲
        if childern is not None:
            childern.parent=node.parent
        # 找孩子
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=childern
            else:
                node.parent.left=childern#
        else:
            self.root=childern


    def is_right(self,node):
        return node==node.parent.right

#遍历:
    def qianxu(self,node):
        if not Node:
            return None
        print(node.data)
        self.qianxu(node.left)
        self.qianxu(node.right)
    def zhonxu(self,node):
        if not Node:
            return None
        self.qianxu(node.left)
        print(node.data)
        self.qianxu(node.right)

    def houxu(self,node):
        if not Node:
            return None
        self.qianxu(node.left)
        self.qianxu(node.right)
        print(node.data)

# 栈实现遍历:
    def qian(self,node):
        stack=[]
        while node and len(stack)>0:
            while node:
                print(node.data)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
