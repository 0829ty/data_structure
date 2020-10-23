class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
# 删除特定节点 203/237
def remove_element(head,val):
    dumy=Node(0)
    dumy.next=head
    cur=dumy
    while cur.next:
        if cur.next.data==val:
            temp=cur.next
            cur.next=cur.next.next
            temp.next=None
        else:
            cur=cur.next
    pre = dumy.next
    while pre:
        print(pre.data,end='->')
        pre=pre.next
    return pre

# 俩俩交换位置
def sawppairs(head):
    dummy=Node(0)
    dummy.next=head
    pre=dummy
    # pre 的后面必须有俩个才循环
    while pre.next and pre.next.next:
#             指针上岗
        slow=pre.next
        fast=pre.next.next
#             交换位置
        pre.next=fast
        slow.next=fast.next
        fast.next=slow
        # 结点前进
        pre=pre.next.next
    return dummy.next

# 俩个有序链表合并(归并排序)
def mergeTwoLists(l1: Node,l2 : Node):
    # 另外创建一个空间
    dummy=Node(0)
    cur=dummy
    while l1 and l2 :
        if l1.data<l2.data:
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
    pre=dummy.next
    while pre:
        print(pre.data,end='->')
        pre=pre.next


if __name__ == '__main__':
    n=Node(1)
    n1=Node(2)
    n2=Node(3)
    n3=Node(4)
    n.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=None
    n4=Node(1)
    n5=Node(1)
    n6=Node(2)
    n7=Node(3)
    n8=Node(4)
    n9=Node(5)
    n4.next=n5
    n5.next=n6
    n6.next=n7
    n7.next=n8
    n8.next=n9
    n9.next=None
    # print(mergeTwoLists(n,n4))
    print(remove_element(n,2))
    # sawppairs(n)
    # output(n1)
    # remove_element(n,2)

    # print()
    # output(n)

