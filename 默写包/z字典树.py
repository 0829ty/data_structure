class TrieNode:
    def __init__(self):
        self.data={}
        self.is_word=False
    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
#      记录根结点
        node=self.root
#       遍历插入结点:
        for char in word:
            child=node.data.get(char)
            if child is None:
                node.data[char]=TrieNode()
            node=node.data[char]
        node.is_word=True
    def search(self,word):
        node = self.root
        #       遍历插入结点:
        for char in word:
            node= node.data.get(char)
            if node is None:
                return False
        return node.is_word
    def prefix(self,prefix):
        node = self.root
        #       遍历插入结点:
        for char in prefix:
            node= node.data.get(char)
            if node is None:
                return False
        return True
if __name__ == '__main__':
    t=Trie()
    t.insert("queue")
    t.insert("quite")
    t.insert("and")
    print(t.search("queue"))
    print(t.prefix("q"))
    print(t.root.data)