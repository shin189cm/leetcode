"""
できなかったこと。
・そもそも問題に何を求められているか分かっていなかった。
作るもの: push, pop, peek, empty を持つ Queue クラス
使える道具: append()（末尾追加）と pop()（末尾削除）しか許されない2つのStack（リスト）

・StackとQueueの違いを分かっていなかった
Stack：LIFO。末尾をtopやpeekと呼ぶ。積み重ねのtop。
Queue：FIFO。先頭をfrontと呼び、末尾をbackと呼ぶ。

・バインド。
__init__でローカル変数を定義してreturnすると、他のメソッドが参照できなくなる。self.in_stack = []とselfにバインドする必要がある

・elseの後ろにコロン

・クラス内部のみで使うメソッドは_から始める

・in_stackを新規受付、out_stackを順番待ち列と考える

"""
class MyQueue:
    """
    
    """
    def __init__(self):
        listx = []
        return listx

    def push(self, x: int) -> None:
        listx.append[x]

    def pop(self) -> int:
        pop = listx[0]
        listy = listx[1:]
        return listx[0]

    def peek(self) -> int:
        return listx[0]

    def empty(self) -> bool:
        if len(listx) == 0:
            return TRUE
        else
            return FALSE
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
