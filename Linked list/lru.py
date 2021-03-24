"""
基于dict和双向链表实现LRU算法
save(key, value)，首先在 HashMap 找到 Key 对应的节点，如果节点存在，更新节点的值，并把这个节点移动队头。如果不存在，需要构造新的节点，
并且尝试把节点塞到队头，如果LRU空间不足，则通过 tail 淘汰掉队尾的节点，同时在 HashMap 中移除 Key。
get(key)，通过 HashMap 找到 LRU 链表节点，把节点插入到队头，返回缓存的值。
"""

# 构建链表节点


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return '%s({%s:%s})' % (__class__.__name__, self.key, self.value)


class DoubuleLinkedList(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def _add_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node

    def _add_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    def _remove_head(self):
        if self.head is None:
            return None
        cur = self.head
        if cur.next is None:
            self.head = self.tail = None
        else:
            cur.next.prev = None
            self.head = cur.next
        self.size -= 1
        return cur

    def _remove_tail(self):
        if self.tail is None:
            return None
        cur = self.tail
        if cur.prev is None:
            self.head = self.tail = None
        else:
            cur.prev.next = None
            self.tail = cur.prev
        self.size -= 1
        return cur

    def remove(self, node=None):
        if not node:
            node = self.tail

        if node == self.head:
            self._remove_head()
        elif node == self.tail:
            self._remove_tail()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1
        return node

    def add_head(self, node):
        return self._add_head(node)

    def append(self, node):
        """
        添加尾部节点
        :param node: 待追加的节点
        :return: 尾部节点
        """
        return self._add_tail(node)

    def print(self):
        """
        打印当前链表
        :return:
        """
        node = self.head
        line = ''
        while node:
            line += '%s' % node
            node = node.next
            if node:
                line += '=>'
        print(line)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.list = DoubuleLinkedList(capacity)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key)
        if not node:
            return -1
        self.list.remove(node)
        self.list.add_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map:
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                if old_node:
                    del self.map[old_node.key]
            node = Node(key, value)
            self.map[key] = node
            self.list.add_head(node)

        else:
            node = self.map.get(key)
            node.value = value
            self.list.remove(node)
            self.list.add_head(node)


if __name__ == "__main__":
    cache = LRUCache(6)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    print(cache.map)
    cache.list.print()
    # print(cache.get(4))
    # cache.list.print()
    # print(cache.get(3))
    # cache.list.print()
    # print(cache.get(2))
    # print(cache.get(1))
    #
    # cache.put(5, 5)
    # print(cache.get(1))
    # cache.list.print()
    # print(cache.get(2))
    # print(cache.get(3))
    # print(cache.get(4))
    # print(cache.get(5))
    # nodes = []
    # # 构建十个节点的双向列表
    # for i in range(10):
    #     node_item = Node(i, i)
    #     nodes.append(node_item)
    # double_linked_list = DoubuleLinkedList(10)
    # double_linked_list.add_head(nodes[0])
    # double_linked_list.print()
    # double_linked_list.add_head(nodes[1])
    # double_linked_list.print()
    # double_linked_list.remove(nodes[0])
    # double_linked_list.print()
