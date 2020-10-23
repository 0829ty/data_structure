#合并有序链表
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
def aaa(l1,l2):
    dummy=Node(0)
    cur=dummy
    while l1 or l2 :
        if (l1.data)<(l2.data):
            cur.next=Node(l1.data)
            l1=l1.next
        else:
            cur.next=Node(l2.data)
            l2=l2.next
        cur=cur.next
        if l1 is None:
            cur.next=l2
            break
        if l2 is None:
            cur.next=l1
            break

        pre = dummy.next
        while pre:
            print(pre.data, end='->')
            pre = pre.next
def bbb(l1,l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2 :
        if (l1.data)<(l2.data):
            cur.next=Node(l1.data)
            l1=l1.next
        else:
            cur.next=Node(l2.data)
            l2=l2.next
        cur=cur.next
    if l1 is None:
        cur.next=l2
    if l2 is None:
        cur.next=l1

    pre = dummy.next
    while pre:
        print(pre.data, end='->')
        pre = pre.next

if __name__ == '__main__':
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    n7=Node(1)
    n8=Node(3)
    n9=Node(5)
    n10=Node(7)


    n7.next=n8
    n8.next=n9
    n9.next=n10
    n10.next=None
    print(bbb(n1,n7))
