class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class Linllist:
    # 维护属性
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    # 添加结点

    def insert(self,index : int,data):
        new_node=Node(data)
        # 判断边界
        if index<0 or index>self.size:
            raise IndexError("The index is out of range")
        elif self.size==0:
            self.head=new_node
            self.tail=new_node

        elif index==0:
            new_node.next=self.head
            self.head=new_node
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        else:
            pre=self.get(index-1)
            new_node.next=pre.next
            pre.next=new_node
        self.size+=1
        return self.size
#    删除
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
            self.tail=pre
        else:
            pre=self.get(index-1)
            remove_node=pre.next
            pre.next=remove_node.next
            remove_node.next=None
        self.size-=1
    # def remove_node(self,data):
    #     temp=self.head
        
        pre=None
        cur=self.head
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        self.head=pre

    def __repr__(self):
        curr=self.head
        string=""
        while curr:
            string+="{}->".format(curr)
            curr=curr.next
        return string+"END"

s=Linllist()

s.insert(0,5)

print(s)



