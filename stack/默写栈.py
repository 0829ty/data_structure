# 1.链表实现
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"


class Stack_link:
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
            raise IndexError("Empty Stack")
        else:
            remove_top=self.top
            self.top=remove_top.next
            remove_top.next=None
        self.size-=1
        return remove_top
    def is_empty(self):
        if self.top is None:
            print("The Stack is empty")
        else:
            print('非空')
    def Stack_size(self):
        return self.size
    def __repr__(self):
        curr=self.top
        string=""
        while curr:
            string+=f"{curr}-->"
            curr=curr.next
        return string+'END'

if __name__ == '__main__':
    s=Stack_link()
    for i in range(10):
        s.push(i)
    print(s)
