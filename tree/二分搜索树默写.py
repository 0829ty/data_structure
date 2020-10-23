from pprint import pformat


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
    def __repr__(self):
        if self.right is None and self.left is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)} ,indent=1)
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
    #     创建结点
        node=Node(value)
    #     判断是否为空
        if self.is_empty():
            self.root=node
        else:
    #        记录根节点
            parent_node=self.root
    # 遍历
            while True:
    #   判断插入值与根节点大小
                if value>parent_node:
                    # 判断右孩子是否为空
                    if parent_node.right is None:
                        parent_node.right=node
                        break
                    else:
                        parent_node=parent_node.right
                else:

                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:#结点下移
                        parent_node=parent_node.left
                # 找父亲
                node.parent=parent_node
    def search(self,value):
    #     判断是否为空
        if self.is_empty():
            raise IndexError("empty")
        else:
            node=self.root
            while node and node.data!=value:
                if value<node.data:
                    node=node.left
                else:
                    node=node.right
            return node
    def is_right(self,node):
        pass
    def __reassign_node(self,node,new_children):
        if new_children is not None:
            new_children.parent=node.parent
        if node.parent is not None:
            pass







    def __str__(self):
        return str(self.root)
    def is_empty(self):
        return True if self.root else False