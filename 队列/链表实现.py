class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
class QueueLink:
    def __init__(self):
        self.head=None
        self.size=0
        self.tail=None

    def enqueue(self,data):
        new_node=Node(data)
        if self.head is None :
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1
    def dequeue(self):
        if self.head is None:
            raise IndexError("空队列")
        else:
            remove_node=self.head
            self.head=remove_node.next
            remove_node.next=None
            self.size-=1
        return remove_node

    def is_empty(self):
        return  self.head is None
    def __repr__(self):
        pre=self.head
        string=""
        while pre:
            string+=f"{pre}->"
            pre=pre.next
        return string+"End"
if __name__ == '__main__':
    # n1=Node(1)
    # n2=Node(2)
    # n3=Node(3)
    # n4=Node(4)
    # n5=Node(5)
    # n6=Node(6)
    n=QueueLink()
    n.enqueue(1)
    n.enqueue(2)
    print(n)
    n.dequeue()
    print(n)




