class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return f"Node({self.data})"
class Tree:
    def __init__(self):
        self.root=None#根节点
    def add (self,item):
        new_node=Node(item)
        if self.root is None:
            self.root=new_node
        else:
            temp=[self.root]#数组实现
            while True:
                pop_root=temp.pop(0)
                if pop_root.left is None:
                    pop_root.left=new_node
                    return
                elif pop_root.right is  None:
                    pop_root.right = new_node
                    return
                else:
                    temp.append(pop_root.left)
                    temp.append(pop_root.right)
    def get_tree(self,item):
        if self.root.data==item:#一层层
            return None #根节点没有父
        temp=[self.root]#数组收集
        while temp:
            pop_node=temp.pop(0)
            if pop_node.left.data ==item:
                return pop_node
            if pop_node.right.data==item:
                return  pop_node
            if pop_node.left is None:
                temp.append(pop_node.left)
            if pop_node.righ is None:
                temp.append(pop_node.righ)
        return  None

if __name__ == '__main__':
    t=Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    print(t.root.left.left)
    print(t.get_tree(3))
