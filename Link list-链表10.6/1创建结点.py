from typing import List
class Node:#创建一个结点(结点元素,结点指向)
    def __init__(self,data,next=None):
        self.data=data
        #结点的指向默认为None
        self.next=None
    def __repr__(self):#将结点表示为一个字符串
        return "Node({})".format(self.data)

# n=Node(1)
# n1=Node(2)
# n.next=n1


class LinkList:
    def __init__(self):
        self.head=None
    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)
#中间插入
    def insert(self,data,i : int):
        new_node=Node(data)    
        if self.head is None and i==1:
            self.insert_head(data)
        else:
            j=1#记录遍历了几步
            #变量接收遍历结果
            temp=self.head
            pre=temp#pre为新结点前一个结点变量
            while j<i:
                pre=temp#pre等于旧temp
                temp=temp.next#temp走一步
                j+=1
            pre.next=new_node
            new_node.next=temp
#列表转化为链表
    def link(self, obj : List):
        # 头部是列表第一个元素
        self.head=Node(obj[0])
        temp=self.head
        for i in obj[1:]:
            # 遍历时创建结点
            node=Node(i)
            # temp指向下一个新结点
            temp.next=node
            # temp等于新结点即遍历的下一个结点
            temp=temp.next
            
#删除头结点
    def remove_head(self):
        temp=self.head
        if temp:
            self.head=temp.next

# # 删除尾部结点 
    def remove_last(self):
        temp=self.head
        if self.head:
            if self.head.next is None:#只有一个结点
                self.head=None
            else:
                while temp.next.next :
                    temp=temp.next
                temp.next =None 

        
    def __repr__(self):
        cur=self.head
        string=""
        while cur:
            string+="{}-->".format(cur)
            cur=cur.next
        return string+"End"
a=LinkList()
# a.insert_head(1)
# a.insert_head(2)
# a.append(3)
# a.insert(4,3)
a.link([6,2,3,4,5,9])
# a.remove_head()
a.remove_last()
print(a)





def name():
    print("ddd")
    return "1"
name()
print(name())

