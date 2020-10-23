class Queue:
    def __init__(self):
        self.entries=[]
        self.size=0
    def enqueue(self,data):
        self.entries.append(data)
        self.size+=1
        return self.entries
    def dequeue(self):
        stemp=self.entries[0]
        self.entries=self.entries[1:]
        self.size-=1
        return stemp
    def get(self,index):
        stemp=self.entries[index]
        return stemp
    def size_of(self):
        return self.size
    def q__reverse(self):
        self.entries=self.entries[::-1]
        return self.entries
    def __repr__(self):
        return f"{self.entries}"
if __name__ == '__main__':
    q=Queue()
    for i in range(5):
        q.enqueue(i)

    # print(q)
    q.dequeue()
    # print(q.get(4))
    # print(q.size_of())
    print(q)
    print(q.q__reverse())

