# 创建结点
from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
# n=Node(1)
# print(n)
# 创建链表
class LinkList:
    def __init__(self):
        # 初始化结点
        self.head=None
# 头部增
    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node
#尾部增加
    def insert_tail(self,data):

        if self.head is None:
            self.insert_head(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)#最后一位指向新结点
#中间插入:
    def insert(self,data,i : int):
        new_node=Node(data)
        if self.head is None and i==1:
            self.insert_head(data)
        else:
            temp=self.head
            j=1
            pre=temp
            while j<i:
                pre=temp
                temp=temp.next
                j+=1
            pre.next=new_node
            new_node.next=temp

#列表转化为链表:
    def Link(self,obj :List):
        self.head=Node(obj[0])
        temp=self.head
        for i in obj[1:]:
            new_node=Node(i)
            temp.next=new_node
            temp=temp.next
#删除头部
    def remove_head(self):
        temp=self.head
        if self.head :
           self.head= temp.next
        temp.next=None# 断开连接.指向空
#删除尾部
    def remove_tail(self):
        temp=self.head
        if self.head:
            if self.head.next is None:
                self.head=None
            else:
                while temp.next.next:
                    temp=temp.next
                temp.next=None

#链表翻转:
    def reverse_Link(self):
        pre=None #变量pre记录前一个
        cur=self.head #cur记录当前位置
        while cur:
            #next_node记录下一步
            next_node=cur.next
            # 转向
            cur.next=pre
            # 向前走一步
            pre=cur
            # 当前位置前进一步
            cur=next_node
        #     头部重置
        self.head=pre
# 索引表
    def Link_index(self,index : int):
        cur=self.head
    #    空链表
        if self.head is None:
            raise IndexError("The linklist is empty")
        for i in range(1,index):
            if cur.next is None:
                raise IndexError("The index is out of range")
            cur=cur.next
        return cur
#更改值:
    def setitem(self, index: int, data):
        cur=self.head
    #    空链表
        if self.head is None:
            raise IndexError("The linklist is empty")
        for i in range(1,index):
            if cur.next is None:
                raise IndexError("The index is out of range")
            cur=cur.next
            cur.data=data
    # def set(self, instance, value):

    def __repr__(self):
        cur=self.head
        string=""
        while cur:
            string+="{}->".format(cur)
            cur=cur.next
        return string+"END"

a=LinkList()
# a.insert_head(1)
# a.insert_head(2)
# a.insert_tail(6)
# a.insert(0,2)
a.Link([1,2,3,4,5])
a.remove_head()
a.remove_tail()
a.reverse_Link()
print(a.Link_index(2))
a.setitem(2,44)


print(a)

