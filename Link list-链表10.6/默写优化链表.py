class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)

class LinkList:
    def __init__(self):
        # 维护属性
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
    #   从0 开始
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def insert(self,index,data):
        # 创建结点
        new_node=Node(data)
        # 判断边界
        if index<0 or index>self.size:
            raise IndexError("索引越界")
        # 空链表
        elif self.size==0:
            self.head=new_node
            self.tail=new_node
        # 头部插入
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        # 尾部插入index从0开始,size-index=1
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        # 中间插入
        else:
            pre= self.get(index-1)
            new_node.next=pre.next
            pre.next=new_node
        self.size+=1
        return self.size
#删除
    def remove(self,index):
        if index<0 or index>self.size:
            raise IndexError("索引越界")
        elif index==0:
            remove_node=self.head
            self.head=remove_node.next
            remove_node.next=None
        elif index==self.size-1:
            remove_node=self.tail
            pre=self.get(index-1)
            pre.next=None
        else:
            pre=self.get(index-1)
            remove_node=pre.next
            pre.next=pre.next.next
            remove_node.next=None
        self.size-=1
        return remove_node
# 翻转
    def reverse(self):
        pre=None
        cur=self.head
        self.tail=cur
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        self.head=pre


    def __repr__(self):
        cur=self.head
        string=""
        while cur:
            # string+="{}->".format(cur)
            string+=f"{cur}->"
            cur=cur.next
        return string+"End"


n=LinkList()
n.insert(0,2)
n.insert(1,1)
n.insert(2,4)
n.insert(3,7)
n.insert(4,8)
print(n.size)
n.insert(5,7)
print(n)
# n.remove(3)
# print(n.remove(3))
n.reverse()
print(n)


