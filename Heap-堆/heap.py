# 左节点下标:2*parent+1,右:2*parent+2
class Heap:
    def __init__(self):
        #初始化堆,数组存储元素,节省存储
        self.data_list=[]
    def get_parent_index(self,child_index):
        #返回父节点下标
        if child_index == 0 or child_index>len(self.data_list)-1:
            return  None# 越界
        else:
            return (child_index-1) >> 1#位移运算.等于index-1)//2 取整

# 交换俩个索引对应的值
    def swap(self,index_a,index_b):
        # 解构交换位置
        self.data_list[index_a],self.data_list[index_b]=self.data_list[index_b],self.data_list[index_a]

    def insert(self,data):
        """
        先把元素放在最后,然后从后往前依次堆化
        以大顶堆为例,如果插入元素大于父节点,则交换位置,直到最后
        """
        self.data_list.append(data)
        index=len(self.data_list)-1
        parent=self.get_parent_index(index)
        #当父级存在,并且添加元素的值大于父集的值,交换位置
        while  parent is not None and self.data_list[index]>self.data_list[parent] :
            self.swap(parent,index)
            index=parent
            parent=self.get_parent_index(parent)
#pop删除元素,堆顶拿出]  \
    def pop(self):
        #记录移除的元素,堆顶
        remove_data=self.data_list[0]
        #替换堆顶替换为末尾元素
        self.data_list[0]=self.data_list[-1]
        #删除堆尾部元素
        del self.data_list[-1]
        # 做堆化,
        self.heapify(0)
        return remove_data
#堆化1从上到下
    def heapify(self,index):
        max_data_index=index
        while True:
            if 2*index+1<len(self.data_list) and self.data_list[2*index+1]>self.data_list[max_data_index]:
                max_data_index=2*index+1
            if 2*index+2<len(self.data_list) and self.data_list[2*index+2]>self.data_list[max_data_index]:
                max_data_index=2*index+2
            if max_data_index==index:
                break
            self.swap(max_data_index,index)
            index=max_data_index

    def __repr__(self):
        return f"{self.data_list}"
if __name__ == '__main__':
    h=Heap()
    for i in range(5):

        h.insert(i+1)
    h.pop()
    print(h)
