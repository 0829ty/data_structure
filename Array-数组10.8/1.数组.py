class Array:#列表来实现数组
    def __init__(self,capacity):#参数是容量
        # 内存大小
        self.array=[None]*capacity
        self.size=0#有效值长度
    # def __repr__(self):
    #     return "{}".format(self.array)
    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def insert(self,index,element):
        #边界条件:索引值小于1
        if index<0 or index>self.size:
            raise IndexError("索引越界")
        # 扩容条件:索引值大于内存大小,或者有效值的长度大于内存的大小
        if index>=len(self.array) or self.size>=len(self.array):
            self.addcapacity()
        for i in range(self.size-1,index-1,-1):
            # 从索引位置开始往后挪一位
            self.array[i+1]=self.array[i]
        #  索引位置等于添加的元素
        self.array[index]=element
        self.size+=1
    def remove(self,index):
#       越界
        if index<0:
            raise IndexError("索引越界")
#         遍历
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1
    def addcapacity(self):
        # 创建新数组为原内存俩倍
        new_array=[None]*len(self.array)*2
        # 遍历有效值长度
        for i in range(len(self.array)):
            # 将旧地址元素复制到新内存里
            new_array[i]=self.array[i]
        #     使用新数组
        self.array=new_array

if __name__ == '__main__':

    a=Array(3)
    a.insert(0,0)
    a.insert(1,1)
    a.insert(2,2)
    a.insert(3,3)
    # a.remove(2)
    # a.addcapacity()
    print(a.array)
    a.output()
    print('----')
    # print(a.size)


