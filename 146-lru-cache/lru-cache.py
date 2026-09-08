class Node:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}  # key -> Node

        self.head = Node()  # least recently used side
        self.tail = Node()  # most recently used side
        self.head.right = self.tail
        self.tail.left = self.head

    def _remove(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _add_recent(self, node):
        previous = self.tail.left
        previous.right = node
        node.left = previous
        node.right = self.tail
        self.tail.left = node

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        node = self.data[key]
        self._remove(node)
        self._add_recent(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.val = value
            self._remove(node)
            self._add_recent(node)
            return

        node = Node(key, value)
        self.data[key] = node
        self._add_recent(node)

        if len(self.data) > self.capacity:
            least_recent = self.head.right
            self._remove(least_recent)
            del self.data[least_recent.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)