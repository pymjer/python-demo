import heapq


class PriorityQueue():
    """docstring for PriorityQueue"""

    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item(object):
    """docstring for Item"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# Example use on a file
if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('HJ'), 3)
    q.push(Item('ZXS'), 10)
    q.push(Item('HLJ'), 8)
    q.push(Item('WS'), 6)
    print(q.pop())
    print(q.pop())
    print(q.pop())
