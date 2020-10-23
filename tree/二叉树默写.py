class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def __repr__(self):
        return f"Node({self.data})"

class Tree:
    def __init__(self):
        # 维护根节点
        self.root=None
    def add(self,data):
        # 创建结点
        new_node=Node(data)
        # 判断是否为空
        if self.root is None:
            # 为空把创建的结点作为根节点
            self.root=new_node
        else:
            # 不为空,遍历树,用数组接收根结点
            temp=[self.root]
            while temp:
                # 将结点弹出
                pop_node=temp.pop(0)
                if pop_node.left is None:
                    # 左孩子为空则添加到左边
                    pop_node.left=new_node
                    return
                if pop_node.right is None:
                    pop_node.right=new_node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)
    def get_tree(self,data):
        if self.root is None:
            return "empty"
        else:
            temp=[self.root]
            while temp:
                # 出队第一个
                pop_node=temp.pop(0)
                if pop_node.left.data==data:
                    return pop_node.left
                if pop_node.right.data == data:
                    return pop_node,pop_node.left
                if pop_node.left is None:
                    temp.append(pop_node.left)
                if pop_node.right is None:
                    temp.append(pop_node.right)
            return None

if __name__ == '__main__':
    t=Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    print(t.root.left.left)
    print(t.get_tree(3))
