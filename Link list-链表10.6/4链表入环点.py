from typing import Optional
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
    def __repr__(self):
        # return "Node({})".format(self.data)
        return f"Node{self.data}"
def detectCirclePoint(head : Optional[Node]=None):
    # optional 可选择的可以是 None 也可以是node
    slow=head#传入头结点
    fast=head
    # 快指针先越界,当快指针指向None停止
    while fast and fast.next :
        fast=fast.next.next
        slow = slow.next
        if slow==fast:
            # return True 判断是否有环
            break
    slow=head#slow回到起点fast继续走
    while slow!=fast:
        slow=slow.next
        fast=fast.next
        return slow#入环点
    # return False
if __name__ == '__main__':

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
    n6.next=n2
    # print(cir(n))
    print(detectCirclePoint(n))


