class TrieNode:
    def __init__(self):
        self.data={}
        self.is_word=False
    def __repr__(self):
        return str(self.data)
class Trie:#{'s':{'o':{'m':{'e':{}}}}
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root#插入结点时,从根节点判断,根节点是一个空字点.
        for chr in word:
            child=node.data.get(chr)#如果当前结点没有元素,则添加结点
            if child is None:
                node.data[chr]=TrieNode()#本级字典添加新字典
            node=node.data[chr]#判断结点下移索引
        node.is_word=True
    def search(self,word):
        node=self.root
        for char in word:
            node=node.data.get(char)#结点下移
            if not node:
                return False
        return node.is_word #判断单词是否为完整的存在树里,so 返回就是False

    #判断prefix是否存在;
    def startWith(self,prefix):
        node=self.root
        for char in prefix:
            node=node.data.get(char)
            if not node:
                return False
        return True


if __name__ == '__main__':
    trie=Trie()
    trie.insert("some")
    trie.insert("see")
    trie.insert("asd")
    print(trie.root.data)
    print(trie.search("so"))
    print(trie.startWith("so"))