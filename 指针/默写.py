class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
class Link_list:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        new_top=Node(data)
        if self.top is None:
            self.top=new_top
        else:
            new_top.next=self.top
            self.top=new_top
        self.size+=1
    def pop(self):
        if self.top is None:
            raise IndexError("空栈")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        self.size-=1
    def __repr__(self):
        curr=self.top
        string=""
        while curr:
            string+=f"{curr}-->"
            curr=curr.next
        return string+'END'

if __name__ == '__main__':
    stack = Link_list()
    for i in range(10):
        stack.push(i)
    print(stack.top)
    print(stack.size)
    for i in range(5):
        stack.pop()
    print(stack)

