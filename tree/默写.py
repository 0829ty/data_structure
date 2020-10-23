from pprint import pformat


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.parent=None
    def __repr__(self):
        if self.right is None and self.left is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)})
class Tree:
    def __init__(self):
        self.root=None
    def __insert(self,data):
        node=Node(data)
        if self.is_empty():
            self.root=node
        else:
            parent_node=self.root
            while True:
                if data<=parent_node.data:
                    if parent_node.left is None:
                        parent_node.left=node
                        break
                    else:
                        parent_node=parent_node.left
                else:
                    if data > parent_node.data:
                        if parent_node.right is None:
                            parent_node.right = node
                            break
                        else:
                            parent_node = parent_node.left
                node.parent=parent_node

    # 遍历递归版:
    # 前序"
    def qianxu(self,node):
        if node is None:
            return None
        else:
            print(node.data)
            self.qianxu(node.left)
            self.qianxu(node.right)
    def zhonxu(self,node):
        if node is None:
            return None
        else:
            self.zhonxu(node.left)
            print(node.data)
            self.zhonxu(node.right)
    def houxu(self,node):
        if node is None:
            return None
        else:
            self.houxu(node.left)
            self.houxu(node.right)
            print(node.data)
    # 栈实现遍历
    def qianxu1(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node.data)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
    def zhonxu1(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node.data)
                node=node.right

    def remove(self,data):
        if self.root is None:
            raise IndexError("empty")
        else:
            node=self.search(data)
            if node.right is None and node.left is None:
                self.ressagin(node,None)
            elif node.right is None:
                self.ressagin(node,node.left)
            elif node.left is None:
                self.ressagin(node,node.right)
            else:
                tmp_node=self.get_max(node)
                self.remove(tmp_node.data)
                node.data=tmp_node.data

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    def is_right(self,node):
        return node==node.parent.right
    def __str__(self):
        return str(self.root)

    def search(self,data):
        if self.root is None:
            raise IndexError("empty")
        else:
            node=self.root
            while node and node.data!=data:
                if data<node.data:
                    node=node.left
                if data>node.data:
                    node=node.right
            return node
        
    def ressagin(self,node,children):
        if children is not None:#如果当前结点子结点不为空
            children.parent=node.parent#子节点和当前结点互换位置,找父亲
        if node.parent is not None:#互换位置后如果当前结点有父结点判断父亲是否为空
            if self.is_right(node):#判断是左还是右
                node.parent.right=children#找孩子
            else:
                node.parent.left=children#删除根节点
        else:
            self.root=children


    def get_max(self,node):
        if self.root is None:
            return None
        else:
            while node.right:
                node=node.right
        return node
    def insert(self,*datas):
        for i in datas:
            self.__insert(i)
        return self


if __name__ == '__main__':

    s=Tree().insert(8,3,1,6,10)
    # s.insert(1,8)
    # s.insert(2)
    # print(s.search(2))
    s.remove(3)
    # s.zhonxu(s.root)
    # s.qianxu(s.root)
    # s.houxu(s.root)
    # print(s.search(3))
    print(s)