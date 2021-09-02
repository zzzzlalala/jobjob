import collections


class LRUCache1(collections.OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class LinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity):
        self.cache = dict()
        # head和tail作为伪头部和尾部
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    # 四个操作(添做头部，移除node，移到头部，移除尾部)
    def addTohead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addTohead(node)

    def removeTail(self, node):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key):
        # 不存在返回-1，存在返回value并且把它放到头部
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        # 不存在就用key 和 value 创建一个新的节点，并添加到头部，size+1，并且放到cache中。
        # 判断容量>capa,删除尾部，size-1
        # 存在的话就返回key和value，并放到头部
        if key not in self.cache:
            node = LinkedNode(key, value)
            self.cache[key] = node
            self.addTohead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail(node)
                self.cache.pop(removed.key)
                self.size -= -1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


if __name__ == '__main__':
    test = LRUCache2(2)
    test.put(1, 1)
    test.put(2, 2)
    print(test.get(1))
    test.put(3,3)
    print(test.get(2))
    test.put(4,4)
    print(test.get(1))
    print(test.get(3))
    print(test.get(4))

print(test.cache)
print(test.cache.values(),test.cache.keys())
print(list(test.cache.values()))
print(list(test.cache.keys()))

