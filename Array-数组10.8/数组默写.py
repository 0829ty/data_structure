class Array:
    def __init__(self,capacity):
        self.array=[None]*capacity#内存大小
        self.size=0#有效数组长度
    def insert(self,index,data):
        # 判断边界
        if index<0 or index>self.size:#防止不连续输入
            raise IndexError("索引越界")
        # 扩容
        if index>=len(self.array) or self.size>=len(self.array):
            self.addcapacity()

        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.array[index]=data
        self.size+=1

#扩容
    def addcapacity(self):
        new_array=[None]*len(self.array)*2
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
#删除
    def remove(self,index):
        # 边界判断
        if index<0:
            raise IndexError("索引越界")
        if self.size>=len(self.array):
            self.addcapacity()
        # 删除
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1

# 输出

    def output(self):
        string=""
        for i in range(self.size-1):
            string+="{}->".format(self.array[i])
        print(string,f"{self.array[self.size-1]}")



if __name__ == '__main__':

    a=Array(3)
    a.insert(0,0)
    a.insert(1,1)
    a.insert(2,2)
    # a.insert(3,3)
    # a.remove(2)
    # a.addcapacity()
    print(a.array)
    a.output()
    # a.output()
    # print('----')
    # print(a.size)