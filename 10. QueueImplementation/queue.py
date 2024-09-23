class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, items):
        if isinstance(items, list):
            self.queue.extend(items)
        else:
            self.queue.append(items)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
        
    def size(self) -> int:
        return len(self.queue)

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue([1, 5, 8])
    print(q.queue)
    q.enqueue(10)
    print(q.queue)
    q.dequeue()
    print(q.queue)
    print(q.size())
    print(q.dequeue(), q.queue)
    print(q.is_empty())