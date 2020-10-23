class Stack:
    def __init__(self):
        #数组用列表存储
        self.data=[]
        self.size=0
    def __str__(self):
        return f"{self.data}"

    def push(self,data):
        self.data.append(data)
        self.size+=1
    def pop(self):
        if len(self.data)!=0:
            temp=self.data.pop()
            self.size-=1
        else:
            raise IndexError("空栈")
        return temp
    def peek(self):
        if self.data:
            return self.data[-1]
    def is_empty(self):
        if self.size==0:
            return "空哒"
        else:
            return '非空'
    def sizqe(self):
        return self.size

if __name__ == '__main__':
    s=Stack()
    for i in range (11):
        s.push(i)

    # print(s.pop())
    # print(s.sizqe())
    # print( s.is_empty())

    print(s)







