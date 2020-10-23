class Node:#创建一个结点(结点元素,结点指向)
    def __init__(self,data,next=None):
        self.data=data
        #结点的指向默认为None
        self.next=None
    def __repr__(self):#将结点表示为一个字符串
        return "Node({})".format(self.data)

class Stack:
    def __init__(self):
        self.size=0
        self.head=None

# 压栈
    def push(self,data):
        new_node = Node(data)
        if self .head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1
    def pop(self):
        if self.head:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.size -= 1
            return temp
        else:
            raise IndexError("空栈")
    def __repr__(self):
        curr=self.head
        string=""
        while curr:
            string+=f"{curr}-->"
            curr=curr.next
        return string+'END'

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack.head)
    print(stack.size)
    for i in range(5):
        stack.pop()
    print(stack)



