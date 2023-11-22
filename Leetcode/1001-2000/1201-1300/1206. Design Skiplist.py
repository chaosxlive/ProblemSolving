# https://leetcode.com/problems/design-skiplist/

from random import random


class Skiplist:

    class SkiplistNode:

        def __init__(self, val=-1):
            self.val = val
            self.prevNodes = [None]
            self.nextNodes = [None]

    def __init__(self):
        self.containerHead = self.SkiplistNode()

    def flipCoin(self) -> bool:
        return random() >= 0.5

    def searchNode(self, target: int) -> SkiplistNode:
        ptr = self.containerHead
        layer = len(self.containerHead.nextNodes) - 1
        while True:
            if ptr.val == target:
                return ptr
            while ptr.nextNodes[layer] != None and target >= ptr.nextNodes[layer].val:
                ptr = ptr.nextNodes[layer]
            if layer != 0:
                layer -= 1
            else:
                if ptr.val == target:
                    return ptr
                return None

    def search(self, target: int) -> bool:
        return self.searchNode(target) != None

    def add(self, num: int) -> None:
        ptr = self.containerHead
        layer = len(self.containerHead.nextNodes) - 1
        newNode = self.SkiplistNode(num)
        while True:
            while ptr.nextNodes[layer] != None and num >= ptr.nextNodes[layer].val:
                ptr = ptr.nextNodes[layer]
            if layer != 0:
                layer -= 1
            else:
                break
        newNode.nextNodes[layer] = ptr.nextNodes[layer]
        if ptr.nextNodes[layer] != None:
            ptr.nextNodes[layer].prevNodes[layer] = newNode
        newNode.prevNodes[layer] = ptr
        ptr.nextNodes[layer] = newNode

        while self.flipCoin():
            if len(newNode.nextNodes) == len(self.containerHead.nextNodes):
                self.containerHead.nextNodes.append(newNode)
                self.containerHead.prevNodes.append(None)
                newNode.nextNodes.append(None)
                newNode.prevNodes.append(self.containerHead)
            else:
                ptr = newNode.prevNodes[layer]
                while layer + 1 >= len(ptr.nextNodes):
                    ptr = ptr.prevNodes[layer]
                layer += 1
                newNode.nextNodes.append(ptr.nextNodes[layer])
                newNode.prevNodes.append(ptr)
                if ptr.nextNodes[layer] != None:
                    ptr.nextNodes[layer].prevNodes[layer] = newNode
                ptr.nextNodes[layer] = newNode

    def erase(self, num: int) -> bool:
        node = self.searchNode(num)
        if node == None:
            return False

        for layer in range(len(node.nextNodes)):
            node.prevNodes[layer].nextNodes[layer] = node.nextNodes[layer]
            if node.nextNodes[layer] != None:
                node.nextNodes[layer].prevNodes[layer] = node.prevNodes[layer]

        del node

        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
