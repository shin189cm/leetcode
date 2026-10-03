class Trie:

    def __init__(self):
        self.word = word
        self.prefix = prefix
        self.result = list([])

        return self.result

    def insert(self, word: str) -> None:
        self.result.append(word)

    def search(self, word: str) -> bool:
        for item in self.result:
            if item == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for item in self.result:
            for i,letter in enumerate(prefix):
                while letter == item[i]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
