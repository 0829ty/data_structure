class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"

def insertSortLinlk(head:Node):
    dummy=Node(0)#虚拟结点,新链表
    pre=dummy
    # 遍历原链表
    cur=head#已经拿到的牌
    while cur is not None:#吧待排序的结点遍历一遍
        temp=cur.next#记录下一个牌
        # 对排序好的链表遍历,找到带插入的结点
        while pre.next and pre.next.data<cur.data:
            pre=pre.next#向后走一步
        # 已确定插入位置,完成插入/
        cur.next=pre.next#安排后事
        pre.next=cur#处理前面的结点
    #     pre ,cur 改变(为下一次循环准备)
        cur=temp
        pre=dummy
    now=dummy.next
    string=""
    while now:
        string+=f"{now}->"
        now=now.next
    return string+"End"
    # return dummy.next

 #
 #
 # def insertionSortList(self, head: Node) -> Node:
 #        # 找个排头
 #        dummy = Node(float("-inf"))
 #        pre = dummy
 #        tail = dummy
 #        # 依次拿head节点
 #        cur = head
 #        while cur:
 #            if tail.val < cur.val:
 #                tail.next = cur
 #                tail = cur
 #                cur = cur.next
 #            else:
 #                # 把下一次节点保持下来
 #                tmp = cur.next
 #                tail.next = tmp
 #                # 找到插入的位置
 #                while pre.next and pre.next.val < cur.val:
 #                    pre = pre.next
 #                # 进行插入操作
 #                cur.next = pre.next
 #                pre.next = cur
 #                pre= dummy
 #                cur = tmp
 #        return dummy.next

if __name__ == '__main__':

    n=Node(3)
    n1=Node(1)
    n2=Node(4)
    n3=Node(5)
    n.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=None

    print(insertSortLinlk(n))