class Trienode(self):
    self.children = {}
    self.is_end = False

class Trie:

    def __init__(self):
        self.node = Trienode()

    def insert(self, word: str) -> None:
        for letter in word:
            # 再帰的に、childrenを作っていき、1文字ずつのツリーを作成したいのだが、
            # それをどこで実装すればいいのか不明だ。
            if letter not in node:


    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
