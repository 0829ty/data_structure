class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
    def __repr__(self):
        return "Node({})".format(self.data)
def cir(head : Node):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return  True
    return False
if __name__ == '__main__':#代码执行入口,从这里开始执行
    n=Node(1)
    n1=Node(2)
    n2=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(6)
    n.next=n1
    n1.next=n2
    n2.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n4
    print(cir(n))
