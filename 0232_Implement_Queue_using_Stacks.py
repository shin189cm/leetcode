class MyQueue:
    """
    これは解いたことあるから、アルゴリズムのイメージはできている。
    stackを使ってfifoを達成する、つまりleftpopを実装するには、
    stackに入っているものを、末尾から順に別の配列に流し込み、
    別の配列の末尾からpopしていくことが必要。
    """

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.queue.append(self.stack.pop())
        return self.queue.pop()

    def peek(self) -> int:
        while self.stack:
            self.queue.append(self.stack.pop())
        return self.queue[-1]

    def empty(self) -> bool:
        while self.stack:
            self.queue.append(self.stack.pop())
        return not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
