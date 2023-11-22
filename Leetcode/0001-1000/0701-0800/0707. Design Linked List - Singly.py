# https://leetcode.com/problems/design-linked-list/

class MyLinkedList:
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.ListNode(None)
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        count = -1
        ptr = self.head
        while count < index:
            ptr = ptr.next
            count += 1

        return ptr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = self.ListNode(val, self.head.next)
        self.head.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        newNode = self.ListNode(val)
        ptr.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        count = -1
        ptrPrev, ptr = None, self.head
        while count < index:
            ptrPrev = ptr
            ptr = ptr.next
            count += 1
        newNode = self.ListNode(val)
        ptrPrev.next = newNode
        newNode.next = ptr
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        count = -1
        ptrPrev, ptr = None, self.head
        while count < index:
            ptrPrev = ptr
            ptr = ptr.next
            count += 1
        ptrPrev.next = ptr.next
        del ptr
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)\