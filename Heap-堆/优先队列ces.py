class Queue:
    def __init__(self):
        self.data=[]
        self.size=0
    def enqueue(self,data):
        self.data.append(data)
        self.size+=1
        self.duihuaup()
    def duihuaup(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) >> 1
        temp = self.data[child_index]
        while child_index > 0 and temp > self.data[parent_index]:
            self.data[child_index] = self.data[parent_index]  # 孩子结点从新赋值
            child_index = parent_index  # 孩子结点上移,向着 0 移动
            parent_index = (child_index - 1) >> 1  # 父结点上移
        self.data[child_index] = temp

    def dequeue(self):#出队
        remove_id=self.data[0]
        self.data[0]=self.data[-1]
        del self.data[-1]
        self.size -= 1
        self.duihuadown()
        return remove_id


    def duihuadown(self):
        total_index = self.size - 1  # 数组的长度
        index = 0
        while True:
            maxvalue_index = index  #
            if 2 * index + 1 <= total_index and self.data[2 * index + 1] > self.data[maxvalue_index]:
                maxvalue_index = 2 * index + 1  # 如果左孩子结点大于当前最大节点,最大值索引等于左孩子索引
            if 2 * index + 2 <= total_index and self.data[2 * index + 2] > self.data[maxvalue_index]:
                maxvalue_index = 2 * index + 2  # 如果右孩子结点大于当前最大结点,最大值索引等于右孩子结点
            if maxvalue_index == index:  # 如果
                break
            self.data[index], self.data[maxvalue_index] = self.data[maxvalue_index], self.data[index]
            # self.swap(index, maxvalue_index)  # 交换最大值和和当前值
            index = maxvalue_index  # 当前值等于这一轮的最大值结点

if __name__ == '__main__':
    a=Queue()
    a.enqueue(1)
    a.enqueue(4)
    a.enqueue(6)
    a.enqueue(3)
    print(a.dequeue())
    print(a.data)

        