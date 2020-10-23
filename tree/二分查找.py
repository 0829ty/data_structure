from pprint import pformat
from typing import List


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)
# a=Node(1)
# print(a)
class BST:
    def  __init__(self):
        self.root=None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return  False
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
                if data>parent_node.data:
                    if parent_node.right is None:
                        parent_node.right=node
                        break
                    else:
                        parent_node=parent_node.right
            node.parent= parent_node
    def insert(self,*datas):
        for data in datas:
            self.__insert(data)
        return self
    def search(self,data):
        if self.is_empty():

            raise IndexError("ddd")
        else:
            node=self.root
            while node and node.data!=data:
                if data<=node.data:
                    node=node.left
                else:
                    node=node.right
            return node
    def is_right(self,node):
        return node==node.parent.right

    def __reassign_nodes(self,node,new_children):#找父亲,找孩子
        if new_children is not None:#如果当前结点子结点不为空
            new_children.parent=node.parent#子节点和当前结点互换位置,找父亲
        if node.parent is not None:#互换位置后如果当前结点有父结点判断父亲是否为空
            if self.is_right(node):#判断删除结点是左还是右,然后孩子代替他
                node.parent.right=new_children#找孩子
            else:
                node.parent.left=new_children#删除根节点
        else:
            self.root=new_children
    def remove(self,data):
        if self.root is None:
            raise IndexError("空树")
        else:
            node=self.search(data)#返回值对应的结点
            if node:
                if node.left is None and node.right is None:
                    self.__reassign_nodes(node,None)
                elif node.left is None:
                    self.__reassign_nodes(node,node.right)
                elif node.right is None:
                    self.__reassign_nodes(node,node.left)
                else:#左右孩子都有
                    tmp_node=self.get_max(node.left)#找到 左子树的最大结点
                    self.remove(tmp_node.data)#删除节点
                    node.data=tmp_node.data#不改变树结构,只改变当前结点值
#-------------------------------------------
    # 栈实现前序遍历(8 3 1 6 10)根左右
    def preOrderTravers(self,node):
        stack=[node]#压栈
        while len(stack)>0:
            print(node.data)#打印弹出的结点
            if node.right:#先进后出，先添加右在添加左
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()#弹出结点
        # 递归实现前序遍历

    def preOrderTravers1(self, node):
        if not node:
            return None
        print(node.data)
        self.preOrderTravers1(node.left)
        self.preOrderTravers1(node.right)

    def preOrderTravers2(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                print(node.data)  # 打印弹出的结点
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node = stack.pop()  # 弹出结点
                node=node.right

# -------------------------------------------
# 中序遍历 左根右 1,3,6,8,10
    def in_order_stack(self,node):
        stack=[]
        # 当结点不为空或栈内有元素
        while node or len(stack)>0:
            # 当结点不为空
            while node:
                # 将所有左结点压入栈
                stack.append(node)
                node=node.left
            if len(stack)>0:#当栈不为空
                # 弹出栈顶
                node=stack.pop()
                # 打印栈顶
                print(node.data)
                # 在判断右边
                node=node.right
#递归实现中序遍历
    def in_order_stacck1(self,node):
        if not node:
            return None
        else:
            self.in_order_stack(node.left)
            print(node.data)
            self.in_order_stack(node.right)
#-----------------------------
#层序遍历:
    def cc(self,root : Node):
        from queue import Queue
        if self.root is None:
            return "empty"
        queue=Queue()
        queue.put(root)
        while not queue.empty():
            node=queue.get()
            print(node.data)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)



    def __str__(self):
        return str(self.root)

    def get_max(self, node):
        if node is None:
            node=self.root
        if node is not None:
            while node.right :
                node=node.right
        return node
    def get_min(self,node):
        if node is None:
            node=self.root
        if not self.is_empty():
            while node.left :
                node=node.left
        return node
# -------------------------
# 俩个栈实现后序遍历:
    def post_order_stack(self,node):
        if node is None:
            return False
        else:
            stack1=[]
            stack2=[]
            stack1.append(node)
            while stack1:#找出后序遍历的逆序,存放在stack2
                node=stack1.pop()
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
                stack2.append(node)
            while stack2:#将stack2 里的元素出站,即为后序遍历
                print(stack2.pop().data,end=" ")
#总结版遍历模板:
    def inorderTraversal(self,root: Node)->List:
        white,gray=0,1

# 根节点删除的问题

if __name__ == '__main__':

    n=BST().insert(8,3,1,6,10)
    # print(n.search(5))\
    # n.remove(8)
    # n.preOrderTravers(n.root)
    # n.preOrderTravers1(n.root)
    # n.in_order_stack(n.root)
    n.cc(n.root)
    # n.in_order_stacck1(n.root)
    print(n)