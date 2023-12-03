# https://leetcode.com/problems/all-oone-data-structure/


class LinkListNode:

    def __init__(self, cnt=0, prevNode=None, nextNode=None):
        self.cnt = cnt
        self.strs = set()
        self.prev = prevNode
        self.next = nextNode


class AllOne:

    def __init__(self):
        self.mapToNode = {}
        self.head = LinkListNode()
        self.head.strs.add('')
        self.tail = self.head

    def inc(self, key: str) -> None:
        oriNode = None
        if key in self.mapToNode:
            oriNode = self.mapToNode[key]
            oriNode.strs.remove(key)
        else:
            oriNode = self.head
        nextNode = oriNode.next
        if nextNode is not None:
            if nextNode.cnt == oriNode.cnt + 1:
                self.mapToNode[key] = nextNode
                nextNode.strs.add(key)
            else:
                # Insert node
                node = LinkListNode(oriNode.cnt + 1, oriNode, nextNode)
                oriNode.next = node
                nextNode.prev = node
                self.mapToNode[key] = node
                node.strs.add(key)
        else:
            # Add tail node
            node = LinkListNode(oriNode.cnt + 1, oriNode)
            oriNode.next = node
            self.tail = node
            self.mapToNode[key] = node
            node.strs.add(key)

        if len(oriNode.strs) == 0:
            prevNode = oriNode.prev
            nextNode = oriNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            del oriNode

    def dec(self, key: str) -> None:
        oriNode = self.mapToNode[key]
        oriNode.strs.remove(key)
        prevNode = oriNode.prev
        if prevNode.cnt == oriNode.cnt - 1:
            self.mapToNode[key] = prevNode
            prevNode.strs.add(key)
        elif oriNode.cnt - 1 == 0:
            del self.mapToNode[key]
        else:
            # Insert node
            node = LinkListNode(oriNode.cnt - 1, oriNode.prev, oriNode)
            prevNode.next = node
            oriNode.prev = node
            self.mapToNode[key] = node
            node.strs.add(key)

        if len(oriNode.strs) == 0:
            prevNode = oriNode.prev
            nextNode = oriNode.next
            prevNode.next = nextNode
            if oriNode == self.tail:
                self.tail = prevNode
            else:
                nextNode.prev = prevNode
            del oriNode

    def getMaxKey(self) -> str:
        return next(iter(self.tail.strs))

    def getMinKey(self) -> str:
        if self.head.next is None:
            return ''
        return next(iter(self.head.next.strs))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
